# coding: utf-8
from django.contrib import admin

from modelpage.bid.models import Entry
from modelpage.bid.forms import EntryForm


class EntryAdmin(admin.ModelAdmin):
    list_display = ('description', 'process', 'price', 'admin_attach')
    search_fields = ('description',)
    date_hierarchy = 'created'
    form = EntryForm


admin.site.register(Entry, EntryAdmin)
