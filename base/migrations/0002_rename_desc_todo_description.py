# Generated by Django 5.0.1 on 2024-02-13 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='desc',
            new_name='description',
        ),
    ]
