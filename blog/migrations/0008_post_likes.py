# Generated by Django 4.1 on 2022-08-11 20:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0007_remove_post_likes_alter_post_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="post_like", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
