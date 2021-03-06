# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False)),
                ('name', models.CharField(help_text='Enter Category name.', max_length=255, verbose_name='Name of Category')),
                ('image', models.ImageField(help_text='An image of the trail_mapper section. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail_category', null=True, verbose_name='Image file', blank=True)),
                ('slug', models.SlugField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Trail Categories',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False)),
                ('name', models.CharField(help_text='Enter Grade name of the Trail.', max_length=255, verbose_name='Grade Name')),
                ('image', models.ImageField(help_text='An image of the trail_mapper grade. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail_grade', null=True, verbose_name='Image file', blank=True)),
                ('slug', models.SlugField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='POI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False)),
                ('name', models.CharField(help_text='Enter name of the Point of Interest.', max_length=255, verbose_name='Name of Point of Interest(POI)')),
                ('notes', models.TextField(help_text='Enter some notes regarding the above named POI', max_length=300, null=True, verbose_name='Notes on named POI', blank=True)),
                ('image', models.ImageField(help_text='An image of the trail_mapper section. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/poi', null=True, verbose_name='Image file', blank=True)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('category', models.ForeignKey(to='trail_mapper.Category')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Points of Interest (POIs)',
            },
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False)),
                ('name', models.CharField(help_text='Enter name of the Trail.', max_length=255, verbose_name='Name of Trail')),
                ('notes', models.TextField(help_text='Enter some notes regarding the above named trail_mapper', max_length=300, null=True, verbose_name='Notes on named Trail', blank=True)),
                ('image', models.ImageField(help_text='An image of the trail_mapper. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail_mapper', null=True, verbose_name='Image file', blank=True)),
                ('colour', models.CharField(help_text='Enter colour hex of the trail_mapper.', max_length=255, null=True, verbose_name='Colour', blank=True)),
                ('offset', models.IntegerField(default=0, help_text='Enter offset value i.e -2', null=True, verbose_name='Offset', blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TrailSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.UUIDField(default=uuid.uuid4, verbose_name='GUID', editable=False)),
                ('name', models.CharField(help_text='Enter name of the Trail.', max_length=255, verbose_name='Name of trail_mapper section')),
                ('notes', models.TextField(help_text='Enter some notes regarding the above named trail_mapper', max_length=300, null=True, verbose_name='Notes on named Trail', blank=True)),
                ('image', models.ImageField(help_text='An image of the trail_mapper section. Most browsers support dragging the image directly on to the "Choose File" button above.', upload_to=b'images/trail_sections', null=True, verbose_name='Image file', blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('time_start', models.DateTimeField(help_text='Enter time when the trail_mapper started on that section.', null=True, verbose_name='Start Time', blank=True)),
                ('time_end', models.DateTimeField(help_text='Enter time when the trail_mapper ended on that section.', null=True, verbose_name='End Time', blank=True)),
                ('grade_id', models.ForeignKey(to='trail_mapper.Grade')),
            ],
            options={
                'verbose_name_plural': 'Trail Section',
            },
        ),
        migrations.CreateModel(
            name='TrailSections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.CharField(help_text='Enter ordering of trail_mapper sections.', max_length=255, verbose_name='Order')),
                ('slug', models.SlugField(null=True, blank=True)),
                ('trail', models.ForeignKey(to='trail_mapper.Trail')),
                ('trail_section', models.ForeignKey(to='trail_mapper.TrailSection')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Trail Sections',
            },
        ),
        migrations.AddField(
            model_name='poi',
            name='trail_section',
            field=models.ForeignKey(to='trail_mapper.TrailSection'),
        ),
    ]
