# Generated by Django 3.2.8 on 2021-12-15 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_user_bio_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_bio',
            new_name='default_user_bio',
        ),
    ]