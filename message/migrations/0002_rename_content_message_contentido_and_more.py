# Generated by Django 4.0.4 on 2022-07-24 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='contentido',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='title',
            new_name='titulo',
        ),
    ]
