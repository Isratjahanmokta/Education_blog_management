# Generated by Django 4.1.5 on 2023-01-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_post', '0004_remove_post_like_count_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]