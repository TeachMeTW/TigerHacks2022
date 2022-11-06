# Generated by Django 4.1.3 on 2022-11-06 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlyBikesApp', '0011_rename_bike_model_user_bikes_user_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bikes',
            field=models.ManyToManyField(blank=True, to='onlyBikesApp.bikemodel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to='onlyBikesApp/static/userprofile'),
        ),
    ]
