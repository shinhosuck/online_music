# Generated by Django 3.2 on 2022-04-20 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_album_create_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='choose_genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='create_genre',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
