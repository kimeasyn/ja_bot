# Generated by Django 2.0.4 on 2018-05-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0007_webdust'),
    ]

    operations = [
        migrations.CreateModel(
            name='NaverSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('level', models.TextField()),
                ('save_at', models.DateTimeField(auto_now_add=True)),
                ('send_at', models.DateTimeField(null=True)),
            ],
        ),
    ]