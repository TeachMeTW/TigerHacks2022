# Generated by Django 4.1.3 on 2022-11-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlyBikesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikemodel',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
