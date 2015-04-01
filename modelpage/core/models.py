# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

# desativado por enquanto
# import uuid
# import os

from filebrowser.fields import FileBrowseField
from tinymce import models as tinymce_models


STATE_CHOICES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)

BANNER_CHOICES = (
    (1, _(u'Super Banner (Home)')),
    (2, _(u'Banner Secundário (Home)')),
    (3, _(u'Popup Banner')),
)

AREA_CHOICES = (
    (1, _(u'Institucional')),
    (2, _(u'Parlamentares')),
    (3, _(u'Secretarias')),
    (4, _(u'Atividade Legislativa')),
    (5, _(u'Serviços')),
    (6, _(u'Transparência')),
    (7, _(u'Assuntos')),
    (8, _(u'Redes Sociais')),
    (9, _(u'Navegação')),
    (10, _(u'RSS')),
    (11, _(u'Imprensa')),
    (12, _(u'Prefeitura')),
    (13, _(u'Câmara')),
    (14, _(u'Contato')),
    (15, _(u'Atendimento')),
    (15, _(u'Atividade')),
)

ORGAO_CHOICES = (
    (1, _(u'Executivo')),
    (2, _(u'Legislativo')),
)


class AreaManager(models.Manager):
    def get_queryset(self):
        return super(AreaManager,
                     self).get_queryset().all()


class AreaVisibleManager(models.Manager):
    def get_queryset(self):
        return super(AreaVisibleManager,
                     self).get_queryset().filter(visible=True)


class Area(models.Model):
    name = models.CharField(_(u'Nome'), max_length=30)
    slug = models.SlugField(_(u'Link no Site'), max_length=200,
                            unique=True)
    visible = models.BooleanField(_(u'Visível no site?'), default=True)
    home = models.BooleanField(_(u'Visível na home?'), default=False)
    order = models.IntegerField(_(u'Ordem no menu'), default=0,
                                help_text='Caso o valor seja zero o menu \
                                ficará em ordem alfabética.')

    objects = AreaManager()
    visibles = AreaVisibleManager()

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Área')
        verbose_name_plural = _(u'Áreas')
        ordering = ['order', 'name']


class Social(models.Model):
    name = models.CharField(_(u'Nome'), max_length=50,
                            help_text='Ex: Facebook')
    link = models.URLField(_(u'Link'),
                           help_text='Ex: http://www.facebook.com/usuario')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Mídia Social')
        verbose_name_plural = _(u'Mídias Sociais')
        ordering = ['name']


class Enterprise(models.Model):
    logo = FileBrowseField(_(u'Logo site'), max_length=200,
                           directory="enterprise/",
                           extensions=[".jpg", ".png"])
    name = models.CharField(_(u'Nome'), max_length=100)
    description = models.CharField(_(u'Descrição'), max_length=100,
                                   blank=True, null=True)
    cnpj = models.CharField(_(u'CNPJ'), max_length=20,
                            help_text='99.999.999/9999-99')
    address = models.CharField(_(u'Endereço'), max_length=200)
    number = models.CharField(_(u'Número'), max_length=10)
    complement = models.CharField(_(u'Complemento'), max_length=100,
                                  blank=True, null=True)
    cep = models.CharField(_(u'CEP'), max_length=9, help_text='99999-999',
                           blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100)
    city = models.CharField(_(u'Cidade'), max_length=100)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES)
    country = models.CharField(_(u'País'), max_length=50)
    phone1 = models.CharField(_(u'Fone 1'), max_length=20,
                              help_text='(99) 9999-9999')
    phone2 = models.CharField(_(u'Fone 2'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    phone3 = models.CharField(_(u'Fone 3 (Fax)'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    email = models.EmailField(_(u'Email'))
    site = models.URLField(_(u'Site'))
    socials = models.ManyToManyField('Social',
                                     verbose_name=_(u'Mídias Sociais'))
    logo_trans = FileBrowseField(_(u'Logo portal da transparência'),
                                 max_length=200, directory="enterprise/",
                                 extensions=[".jpg", ".png"])

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Empresa')
        verbose_name_plural = _(u'Empresa')


class Category(models.Model):
    area = models.ForeignKey('Area', verbose_name=_(u'Área'))
    name = models.CharField(_(u'Nome da Categoria'), max_length=200)
    slug = models.SlugField(_(u'Link no Site'), max_length=200,
                            unique=True)
    acronym = models.CharField(_(u'Sigla'), max_length=50, blank=True,
                               null=True)
    order = models.IntegerField(_(u'Ordem do Menu'), default=0,
                                help_text='Caso o valor seja zero o menu \
                                ficará em ordem alfabética.')
    menu = models.BooleanField(_(u'Visível no menu principal?'), default=False)
    menu_extra = models.BooleanField(_(u'Visível no menu secundário?'),
                                     default=False)
    home = models.BooleanField(_(u'Visível na home?'), default=False)

    def get_absolute_url(self):
        return reverse('blog:category_list', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        a = Area.visibles.get(name=self.area)
        self.home = a.home

        super(Category, self).save(*args, **kwargs)

        c = Content.objects.filter(category=self.pk)
        if not c:
            Content.objects.get_or_create(
                category_id=self.pk, body='Aguardando conteúdo...')


    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Categoria')
        verbose_name_plural = _(u'Categorias')
        ordering = ['area__order', 'area__name', 'order', 'name']


class Content(models.Model):
    category = models.ForeignKey('Category', verbose_name=_(u'Página'),
                                 default=1, unique=True)
    body = tinymce_models.HTMLField(_(u'Conteúdo da Página'))

    def admin_body(self):
        if self.body:
            return self.body[:150]
    admin_body.allow_tags = True
    admin_body.short_description = 'Conteúdo da Página'

    def __unicode__(self):
        return unicode(self.pk)

    class Meta:
        verbose_name = _(u'Página')
        verbose_name_plural = _(u'Páginas')
        ordering = ['category']


class Link(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    link = models.URLField(_(u'Link do Site'))
    image = FileBrowseField(_(u'Logo'), max_length=200,
                            directory="link/", extensions=[".jpg", ".png"])

    def admin_image(self):
        return '<img src="%s" width="120" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Logo do Link'

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Link Útil')
        verbose_name_plural = _(u'Links Úteis')
        ordering = ['name']


class Program(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    link = models.URLField(_(u'Link do Site'))
    image = FileBrowseField(_(u'Logo'), max_length=200,
                            directory="program/", extensions=[".jpg", ".png"])

    def admin_image(self):
        return '<img src="%s" width="120" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Logo do Programa'

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Programa')
        verbose_name_plural = _(u'Programas')
        ordering = ['name']


class BannerManager(models.Manager):
    def get_queryset(self):
        return super(BannerManager,
                     self).get_queryset().all()


class BannerPublishedManager(models.Manager):
    def get_queryset(self):
        return super(BannerPublishedManager,
                     self).get_queryset().filter(publish=True)


class Banner(models.Model):
    # desativado por enquanto
    # def get_file_path(instance, filename):
    #     ext = filename.split('.')[-1]
    #     filename = "%s.%s" % (uuid.uuid4(), ext)
    #     return os.path.join('banner', filename)

    type = models.IntegerField(_(u'Banner'), choices=BANNER_CHOICES, default=1)
    image = FileBrowseField(_(u'Banner'), max_length=200,
                            directory="banner/", extensions=[".jpg", ".png"])
    title = models.CharField(_(u'Título do banner'), max_length=100)
    link = models.URLField(_(u'Link do banner'), blank=True, null=True)
    publish = models.BooleanField(_(u'Visível no site?'), default=True)

    objects = BannerManager()
    published = BannerPublishedManager()

    def admin_image(self):
        return '<img src="%s" width="200" />' % self.image.url
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name = _(u'Banner')
        verbose_name_plural = _(u'Banners')


class Timeline(models.Model):
    title = models.CharField(_(u'Título'), max_length=50)
    description = models.TextField(_(u'Descrição'),
                                   help_text='Uma breve história')
    image = FileBrowseField(_(u'Imagem'), max_length=200,
                            directory="timeline/", extensions=[".jpg", ".png"],
                            blank=True, null=True)
    period = models.CharField(_(u'Ano'), max_length=4, unique=True)

    def admin_image(self):
        if self.image:
            return '<img src="%s" width="200" />' % self.image.url
        else:
            return 'Sem imagem'
    admin_image.allow_tags = True
    admin_image.short_description = 'Imagem'

    def __unicode__(self):
        return "%s (%s)" % (unicode(self.title), self.period)

    class Meta:
        verbose_name = _(u'Linha do Tempo')
        verbose_name_plural = _(u'Linha do Tempo')
        ordering = ['-period']
