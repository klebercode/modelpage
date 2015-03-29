# coding: utf-8
from django.conf.urls import patterns, url

from modelpage.bid.views import EntryListView


urlpatterns = patterns(
    'modelpage.bid.views',
    url(r'^$', EntryListView.as_view(), name='home'),
)
