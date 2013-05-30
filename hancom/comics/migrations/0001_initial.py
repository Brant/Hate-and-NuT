# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comic'
        db.create_table(u'comics_comic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assets_from_images', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=900)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('comic_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'comics', ['Comic'])


    def backwards(self, orm):
        # Deleting model 'Comic'
        db.delete_table(u'comics_comic')


    models = {
        u'comics.comic': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Comic'},
            'assets_from_images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'comic_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '900'})
        }
    }

    complete_apps = ['comics']