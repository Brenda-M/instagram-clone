# Generated by Django 3.0.6 on 2020-05-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200530_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
