# Generated by Django 3.1.1 on 2020-09-21 15:24

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_auto_20200920_2126"),
    ]

    operations = [
        migrations.CreateModel(
            name="Avatar",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to=core.models.user_image_file_path)),
            ],
        ),
    ]
