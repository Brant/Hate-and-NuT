# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'StoryArc.complete'
        db.delete_column(u'comics_storyarc', 'complete')


    def backwards(self, orm):
        # Adding field 'StoryArc.complete'
        db.add_column(u'comics_storyarc', 'complete',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    models = {
        u'characters.character': {
            'Meta': {'ordering': "['-show_first_date', 'index', 'name']", 'object_name': 'Character'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'assets_from_images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'show_first_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'comics.comic': {
            'Meta': {'ordering': "['-chronology']", 'object_name': 'Comic'},
            'assets_from_images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'characters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['characters.Character']", 'null': 'True', 'blank': 'True'}),
            'chronology': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'comic_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'continuation_of': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comics.Comic']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_comic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'preview_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'single_row': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'special_story_arc_title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'story_arc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comics.StoryArc']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '900'})
        },
        u'comics.storyarc': {
            'Meta': {'object_name': 'StoryArc'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        }
    }

    complete_apps = ['comics']