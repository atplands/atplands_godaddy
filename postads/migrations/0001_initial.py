# Generated by Django 3.1.1 on 2022-06-12 10:48

import datetime
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=600)),
                ('message', models.TextField(blank=True, null=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('video_url', embed_video.fields.EmbedVideoField(blank=True, default='https://www.youtube.com/watch?v=DL77F7AWIl8', null=True)),
                ('ad_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
