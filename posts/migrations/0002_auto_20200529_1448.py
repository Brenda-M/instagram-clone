# Generated by Django 3.0.6 on 2020-05-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
