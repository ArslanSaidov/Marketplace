# Generated by Django 4.1.3 on 2023-04-12 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='number',
        ),
    ]
