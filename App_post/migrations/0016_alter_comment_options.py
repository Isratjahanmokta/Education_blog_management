# Generated by Django 4.1.5 on 2023-01-24 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0015_rename_comment_by_comment_commented_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created',)},
        ),
    ]
