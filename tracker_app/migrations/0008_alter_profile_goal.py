# Generated by Django 5.2 on 2025-05-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0007_rename_usergoal_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='goal',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
