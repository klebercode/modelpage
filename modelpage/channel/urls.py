# coding: utf-8
from django.conf.urls import patterns, url

from modelpage.channel.views import (VideoYearArchiveView,
                                     VideoMonthArchiveView,
                                     VideoDayArchiveView, VideoListView,
                                     VideoDateDetailView, VideoTagListView,
                                     VideoCategoryListView,
                                     AudioListView, AudioDateDetailView,
                                     AudioTagListView, AudioCategoryListView,)


urlpatterns = patterns(
    'modelpage.channel.views',
    # video
    url(r'^video/$', VideoListView.as_view(), name='video'),
    # url(r'^video/(?P<year>\d{4})/$',
    #     VideoYearArchiveView.as_view(),
    #     name='video_archive_year'),
    # url(r'^video/(?P<year>\d{4})/(?P<month>\d+)/$',
    #     VideoMonthArchiveView.as_view(month_format='%m'),
    #     name='video_archive_month'),
    # url(r'^video/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
    #     VideoDayArchiveView.as_view(month_format='%m'),
    #     name='video_archive_day'),
    url(r'^video/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+).html$',
        VideoDateDetailView.as_view(month_format='%m'),
        name='video_date_detail'),
    url(r'^video/marcacao/(?P<tag_slug>[-\w]+)/$',
        VideoTagListView.as_view(),
        name='video_tag_list'),
    url(r'^video/categoria/(?P<cat_slug>[-\w]+)/$',
        VideoCategoryListView.as_view(),
        name='video_category_list'),

    # audio
    url(r'^audio/$', AudioListView.as_view(), name='audio'),
    # url(r'^video/(?P<year>\d{4})/$',
    #     VideoYearArchiveView.as_view(),
    #     name='video_archive_year'),
    # url(r'^video/(?P<year>\d{4})/(?P<month>\d+)/$',
    #     VideoMonthArchiveView.as_view(month_format='%m'),
    #     name='video_archive_month'),
    # url(r'^video/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
    #     VideoDayArchiveView.as_view(month_format='%m'),
    #     name='video_archive_day'),
    url(r'^audio/(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[-\w]+).html$',
        AudioDateDetailView.as_view(month_format='%m'),
        name='audio_date_detail'),
    url(r'^audio/marcacao/(?P<tag_slug>[-\w]+)/$',
        AudioTagListView.as_view(),
        name='audio_tag_list'),
    url(r'^audio/categoria/(?P<cat_slug>[-\w]+)/$',
        AudioCategoryListView.as_view(),
        name='audio_category_list'),
)
