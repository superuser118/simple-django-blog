# Generated by Django 4.1 on 2022-08-11 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created"]},
        ),
    ]