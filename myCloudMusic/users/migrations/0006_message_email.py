# Generated by Django 3.2 on 2022-08-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
