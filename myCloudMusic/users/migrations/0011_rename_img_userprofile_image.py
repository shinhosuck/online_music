# Generated by Django 3.2 on 2022-10-05 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userprofile_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='img',
            new_name='image',
        ),
    ]
