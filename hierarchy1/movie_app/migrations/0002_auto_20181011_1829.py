# Generated by Django 2.0.6 on 2018-10-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='pic_url',
            field=models.URLField(null='true'),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='yearReleased',
            field=models.IntegerField(default=0),
        ),
    ]
