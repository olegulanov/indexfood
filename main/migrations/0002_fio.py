# Generated by Django 3.2.8 on 2021-10-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FIO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='имя')),
                ('Surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('Otchevstvo', models.CharField(max_length=40, verbose_name='Отчество')),
                ('Age', models.CharField(max_length=40, verbose_name='Возраст')),
            ],
        ),
    ]