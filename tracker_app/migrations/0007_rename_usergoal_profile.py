# Generated by Django 5.2 on 2025-05-24 12:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0006_usergoal'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserGoal',
            new_name='Profile',
        ),
    ]
