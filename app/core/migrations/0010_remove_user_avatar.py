# Generated by Django 3.1.1 on 2020-09-21 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_avatarimage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="avatar",
        ),
    ]
