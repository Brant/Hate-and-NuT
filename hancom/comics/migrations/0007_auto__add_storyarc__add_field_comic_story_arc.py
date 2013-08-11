# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StoryArc'
        db.create_table(u'comics_storyarc', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'comics', ['StoryArc'])

        # Adding field 'Comic.story_arc'
        db.add_column(u'comics_comic', 'story_arc',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['comics.StoryArc'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'StoryArc'
        db.delete_table(u'comics_storyarc')

        # Deleting field 'Comic.story_arc'
        db.delete_column(u'comics_comic', 'story_arc_id')


    models = {
        u'comics.comic': {
            'Meta': {'ordering': "['-chronology']", 'object_name': 'Comic'},
            'assets_from_images': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'chronology': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'comic_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'single_row': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
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