# Generated by Django 2.0.4 on 2018-05-07 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20180501_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webmusic',
            old_name='content',
            new_name='title',
        ),
    ]
