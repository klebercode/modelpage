from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^construcao.html$', 'modelpage.core.views.construction',
        name='construction'),
    url(r'^$', 'modelpage.core.views.home', name='home'),
    url(r'^ouvidoria.html$', 'modelpage.core.views.contact', name='contact'),

    url(r'^transparencia/$', 'modelpage.core.views.transparency',
        name='transparency'),

    url(r'^(?P<slug>[-\w]+).html$', 'modelpage.core.views.content',
        name='content'),

    url(r'^eventos/', include('modelpage.event.urls', namespace='event')),
    url(r'^noticias/', include('modelpage.blog.urls', namespace='blog')),
    url(r'^licitacoes/', include('modelpage.bid.urls', namespace='bid')),
    url(r'^canais/', include('modelpage.channel.urls', namespace='channel')),

    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

    # tinymce
    url(r'^tinymce/', include('tinymce.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# )
