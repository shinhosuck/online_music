# Generated by Django 3.2 on 2022-10-13 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20221012_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
