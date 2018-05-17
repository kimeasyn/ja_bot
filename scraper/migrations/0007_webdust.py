# Generated by Django 2.0.4 on 2018-05-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0006_auto_20180517_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebDust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('level', models.SmallIntegerField()),
                ('save_at', models.DateTimeField(auto_now_add=True)),
                ('send_at', models.DateTimeField(null=True)),
            ],
        ),
    ]