# Generated by Django 3.2.8 on 2021-10-26 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tovars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tovars',
            old_name='title',
            new_name='title_name',
        ),
    ]