# Generated by Django 4.1.5 on 2023-01-19 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_alter_post_options_remove_post_update_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]