# Generated by Django 2.0.4 on 2018-05-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_auto_20180507_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='webmusic',
            name='rank',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
