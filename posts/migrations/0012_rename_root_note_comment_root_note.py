# Generated by Django 3.2.6 on 2021-10-22 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_rename_post_comment_root_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='root_Note',
            new_name='root_note',
        ),
    ]
