# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from filebrowser.fields import FileBrowseField
from tinymce import models as tinymce_models
from taggit_autosuggest.managers import TaggableManager

from modelpage.current_user import get_current_user
from modelpage.core.models import Category


class EntryManager(models.Manager):
    def get_queryset(self):
        return super(EntryManager,
                     self).get_queryset().all()


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(publish=True, focus=False)


class FocusedManager(models.Manager):
    def get_queryset(self):
        return super(FocusedManager,
                     self).get_queryset().filter(publish=True, focus=True)


class Entry(models.Model):
    created = models.DateTimeField(_(u'Data de Criação'))
    title = models.CharField(_(u'Título da Notícia'), max_length=200)
    slug = models.SlugField(_(u'Link no Site'), max_length=200,
                            unique=True)
    image = FileBrowseField(_(u'Imagem da Capa'), max_length=200,
                            directory="blog/", extensions=[".jpg", ".png"])
    body = tinymce_models.HTMLField(_(u'Texto'))
    publish = models.BooleanField(_(u'Publicar no site?'), default=True)
    focus = models.BooleanField(_(u'Em destaque no início?'), default=False)
    modified = models.DateTimeField(_(u'Data de Modificação'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_(u'Autor'),
                               editable=False, default=get_current_user)
    categories = models.ManyToManyField(Category,
                                        verbose_name=_(u'Categorias'))

    tags = TaggableManager()
    objects = EntryManager()
    published = PublishedManager()
    focused = FocusedManager()

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem da Notícia'

    def get_absolute_url(self):
        return reverse('blog:entry_date_detail',
                       kwargs={'year': self.created.year,
                               'month': self.created.strftime('%m'),
                               'day': self.created.strftime('%d'),
                               'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Notícia')
        verbose_name_plural = _(u'Notícias')
        ordering = ['-created', 'title', 'author']
