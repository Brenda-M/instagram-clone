# Generated by Django 3.0.6 on 2020-06-02 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200601_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='img_post',
        ),
    ]