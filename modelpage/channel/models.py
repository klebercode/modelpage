# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from tinymce import models as tinymce_models
from taggit_autosuggest.managers import TaggableManager

from modelpage.current_user import get_current_user
from modelpage.core.models import Category


class Video(models.Model):
    created = models.DateTimeField(_(u'Data de Criação'))
    title = models.CharField(_(u'Título do Vídeo'), max_length=200)
    slug = models.SlugField(_(u'Link no Site'), max_length=200,
                            unique=True)
    embed = models.TextField(_(u'Código do Vídeo'), help_text='Embed')
    body = tinymce_models.HTMLField(_(u'Descrição do Vídeo'), blank=True,
                                    null=True)
    modified = models.DateTimeField(_(u'Data de Modificação'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_(u'Autor'),
                               editable=False, default=get_current_user)
    categories = models.ManyToManyField(Category,
                                        verbose_name=_(u'Categorias'),
                                        blank=True, null=True)

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('channel:video_date_detail',
                       kwargs={'year': self.created.year,
                               'month': self.created.strftime('%m'),
                               'day': self.created.strftime('%d'),
                               'slug': self.slug})

    def admin_embed(self):
        return self.embed
    admin_embed.allow_tags = True
    admin_embed.short_description = 'Vídeo'

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        self.embed = self.embed.replace('width="560" height="315"',
                                        'width="100%" height="100%"')
        super(Video, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'Canal de Vídeo')
        verbose_name_plural = _(u'Canal de Vídeos')
        ordering = ['-created', 'title', 'author']


class Audio(models.Model):
    created = models.DateTimeField(_(u'Data de Criação'))
    title = models.CharField(_(u'Título do Áudio'), max_length=200)
    slug = models.SlugField(_(u'Link no Site'), max_length=200,
                            unique=True)
    embed = models.TextField(_(u'Código do Áudio'), help_text='Embed')
    body = tinymce_models.HTMLField(_(u'Descrição do Áudio'), blank=True,
                                    null=True)
    modified = models.DateTimeField(_(u'Data de Modificação'), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_(u'Autor'),
                               editable=False, default=get_current_user)
    categories = models.ManyToManyField(Category,
                                        verbose_name=_(u'Categorias'),
                                        blank=True, null=True)

    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('channel:audio_date_detail',
                       kwargs={'year': self.created.year,
                               'month': self.created.strftime('%m'),
                               'day': self.created.strftime('%d'),
                               'slug': self.slug})

    def admin_embed(self):
        return self.embed
    admin_embed.allow_tags = True
    admin_embed.short_description = 'Áudio'

    def __unicode__(self):
        return unicode(self.title)

    def save(self, *args, **kwargs):
        self.embed = self.embed.replace('height="450"', 'height="100%"')
        super(Audio, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u'Canal de Áudio')
        verbose_name_plural = _(u'Canal de Áudios')
        ordering = ['-created', 'title', 'author']
