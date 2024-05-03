# Generated by Django 5.0.2 on 2024-03-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="type",
            field=models.CharField(
                choices=[("self", "self"), ("partner", "partner")],
                default="self",
                max_length=100,
            ),
        ),
    ]