# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Character'
        db.create_table(u'characters_character', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assets_from_images', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('index', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('show_first_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'characters', ['Character'])


    def backwards(self, orm):
        # Deleting model 'Character'
        db.delete_table(u'characters_character')


    models = {
        u'characters.character': {
            'Meta': {'ordering': "['-index', 'name']", 'object_name': 'Character'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'assets_from_images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'show_first_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        }
    }

    complete_apps = ['characters']