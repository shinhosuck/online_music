# Generated by Django 3.2 on 2022-10-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_userprofiles_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
