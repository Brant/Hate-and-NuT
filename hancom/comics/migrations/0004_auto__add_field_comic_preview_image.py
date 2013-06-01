# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comic.preview_image'
        db.add_column(u'comics_comic', 'preview_image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comic.preview_image'
        db.delete_column(u'comics_comic', 'preview_image')


    models = {
        u'comics.comic': {
            'Meta': {'ordering': "['-chronology']", 'object_name': 'Comic'},
            'assets_from_images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'chronology': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'comic_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '900'})
        }
    }

    complete_apps = ['comics']