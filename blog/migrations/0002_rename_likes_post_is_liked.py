# Generated by Django 3.2.20 on 2023-07-26 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='is_liked',
        ),
    ]
