# Generated by Django 5.2 on 2025-04-18 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(model_name="tweet", old_name="user", new_name="author",),
    ]
