# Generated by Django 3.2.3 on 2021-05-31 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_notes_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='author',
        ),
    ]
