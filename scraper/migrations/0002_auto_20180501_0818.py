# Generated by Django 2.0.4 on 2018-05-01 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiweather',
            name='content',
        ),
        migrations.AddField(
            model_name='apiweather',
            name='humidity',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apiweather',
            name='status',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apiweather',
            name='temp',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
