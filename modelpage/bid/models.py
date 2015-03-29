# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField


class Entry(models.Model):
    created = models.DateTimeField(_(u'Data de Criação'), auto_now_add=True)
    modified = models.DateTimeField(_(u'Data de Modificação'), auto_now=True)
    description = models.TextField(_(u'Objeto da Licitação'))
    process = models.CharField(_(u'Processo Licitatório Nº'), max_length=20)
    price = models.CharField(_(u'Tomada de Preços Nº'), max_length=20)
    attach = FileBrowseField(_(u'Arquivo'), max_length=200,
                             directory="licitacao/",
                             extensions=[".pdf", ".doc"])

    def admin_attach(self):
        if self.attach:
            return "<a href='%s'>Baixar</a>" % self.attach.url
        else:
            return "Nenhum arquivo encontrado"
    admin_attach.allow_tags = True
    admin_attach.short_description = _(u'Arquivo')

    def __unicode__(self):
        return unicode(self.process)

    class Meta:
        verbose_name = _(u'Licitação')
        verbose_name_plural = _(u'Licitações')
        ordering = ['-created', 'description', 'process', 'price']
