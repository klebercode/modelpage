# coding: utf-8
from django.contrib import admin

from modelpage.channel.models import Video, Audio


class VideoAdmin(admin.ModelAdmin):
    list_filter = ('created', 'author__username', 'tags',
                   'categories')
    list_display = ('title', 'created', 'author', 'admin_embed')
    search_fields = ('title', 'created', 'author', 'body')
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}


class AudioAdmin(admin.ModelAdmin):
    list_filter = ('created', 'author__username', 'tags',
                   'categories')
    list_display = ('title', 'created', 'author', 'admin_embed')
    search_fields = ('title', 'created', 'author', 'body')
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
