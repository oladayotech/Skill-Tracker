# Generated by Django 5.2 on 2025-05-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='journal_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
