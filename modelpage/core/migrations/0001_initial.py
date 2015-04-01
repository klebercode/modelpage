# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'core_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('home', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'core', ['Area'])

        # Adding model 'Social'
        db.create_table(u'core_social', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Social'])

        # Adding model 'Enterprise'
        db.create_table(u'core_enterprise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cnpj', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('complement', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('phone3', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Enterprise'])

        # Adding M2M table for field socials on 'Enterprise'
        m2m_table_name = db.shorten_name(u'core_enterprise_socials')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('enterprise', models.ForeignKey(orm[u'core.enterprise'], null=False)),
            ('social', models.ForeignKey(orm[u'core.social'], null=False))
        ))
        db.create_unique(m2m_table_name, ['enterprise_id', 'social_id'])

        # Adding model 'Category'
        db.create_table(u'core_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Area'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('acronym', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('menu_extra', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('home', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'core', ['Category'])

        # Adding model 'Content'
        db.create_table(u'core_content', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Category'], unique=True)),
            ('body', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'core', ['Content'])

        # Adding model 'Link'
        db.create_table(u'core_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Link'])

        # Adding model 'Program'
        db.create_table(u'core_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Program'])

        # Adding model 'Banner'
        db.create_table(u'core_banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'core', ['Banner'])

        # Adding model 'Timeline'
        db.create_table(u'core_timeline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
            ('period', self.gf('django.db.models.fields.CharField')(unique=True, max_length=4)),
        ))
        db.send_create_signal(u'core', ['Timeline'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'core_area')

        # Deleting model 'Social'
        db.delete_table(u'core_social')

        # Deleting model 'Enterprise'
        db.delete_table(u'core_enterprise')

        # Removing M2M table for field socials on 'Enterprise'
        db.delete_table(db.shorten_name(u'core_enterprise_socials'))

        # Deleting model 'Category'
        db.delete_table(u'core_category')

        # Deleting model 'Content'
        db.delete_table(u'core_content')

        # Deleting model 'Link'
        db.delete_table(u'core_link')

        # Deleting model 'Program'
        db.delete_table(u'core_program')

        # Deleting model 'Banner'
        db.delete_table(u'core_banner')

        # Deleting model 'Timeline'
        db.delete_table(u'core_timeline')


    models = {
        u'core.area': {
            'Meta': {'ordering': "['order', 'name']", 'object_name': 'Area'},
            'home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'core.banner': {
            'Meta': {'object_name': 'Banner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'core.category': {
            'Meta': {'ordering': "['area__order', 'area__name', 'order', 'name']", 'object_name': 'Category'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Area']"}),
            'home': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'menu_extra': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'core.content': {
            'Meta': {'ordering': "['category']", 'object_name': 'Content'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Category']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.enterprise': {
            'Meta': {'object_name': 'Enterprise'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cnpj': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'complement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'phone3': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'socials': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Social']", 'symmetrical': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'core.link': {
            'Meta': {'ordering': "['name']", 'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.program': {
            'Meta': {'ordering': "['name']", 'object_name': 'Program'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.social': {
            'Meta': {'ordering': "['name']", 'object_name': 'Social'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.timeline': {
            'Meta': {'ordering': "['-period']", 'object_name': 'Timeline'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']
