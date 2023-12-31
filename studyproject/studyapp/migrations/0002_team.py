# Generated by Django 4.2 on 2023-06-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studyapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("img", models.ImageField(upload_to="Pictures")),
                ("desc", models.TextField()),
            ],
        ),
    ]
