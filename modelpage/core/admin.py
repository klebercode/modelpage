# coding: utf-8
from django.contrib import admin
from django.utils.translation import ungettext, ugettext as _

from modelpage.core.models import (Enterprise, Social, Category, Link, Program,
                                   Banner, Content, Timeline, Area)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'phone3', 'email')
    search_fields = ('name', 'description', 'address', 'number', 'complement',
                     'cep', 'district', 'city', 'state',
                     'phone1', 'phone2', 'phone3', 'email')


class AreaAdmin(admin.ModelAdmin):
    list_filter = ('visible', 'home', 'menu')
    list_display = ('name', 'slug', 'visible', 'home', 'menu', 'order')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    actions = ['change_visible']

    def change_visible(self, request, queryset):
        count = 0
        for obj in queryset:
            if obj.visible:
                obj.visible = False
                obj.save()
            else:
                obj.visible = True
                obj.save()
            count = count + 1

        msg = ungettext(
            u'%d área mudou o status de visibilidade no site.',
            u'%d áreas mudaram o status de visibilidade no site.',
            count
        )
        self.message_user(request, msg % count)

    change_visible.short_description = _(u'Mudar Status de Visibilidade')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('area', 'menu', 'menu_extra', 'home')
    list_display = ('name', 'acronym', 'slug', 'area', 'menu', 'menu_extra',
                    'home')
    search_fields = ('name', 'acronym', 'slug', 'area__name')
    prepopulated_fields = {'slug': ('name',)}


class LinkAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'name', 'link')
    search_fields = ('name',)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'name', 'link')
    search_fields = ('name',)


class BannerAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('admin_image', 'title', 'type', 'publish')
    search_fields = ('title',)


class ContentAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('category', 'admin_body')
    search_fields = ('category__name', 'body')


class TimelineAdmin(admin.ModelAdmin):
    list_filter = ('period',)
    list_display = ('title', 'period', 'admin_image', 'description')
    search_fields = ('title', 'period', 'description')


admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Social)
admin.site.register(Area, AreaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Timeline, TimelineAdmin)
