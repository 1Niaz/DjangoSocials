# Generated by Django 5.0.6 on 2024-05-20 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_usermodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]