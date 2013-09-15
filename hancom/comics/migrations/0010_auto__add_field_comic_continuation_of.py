# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comic.continuation_of'
        db.add_column(u'comics_comic', 'continuation_of',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comics.Comic'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comic.continuation_of'
        db.delete_column(u'comics_comic', 'continuation_of_id')


    models = {
        u'comics.comic': {
            'Meta': {'ordering': "['-chronology']", 'object_name': 'Comic'},
            'assets_from_images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'chronology': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'comic_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'continuation_of': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['comics.Comic']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        }
    }

    complete_apps = ['comics']