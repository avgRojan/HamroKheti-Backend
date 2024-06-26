# Generated by Django 5.0.2 on 2024-03-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_rename_name_user_full_name_remove_user_is_agent_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("farmer", "Farmer"),
                    ("delivery_partner", "Delivery Partner"),
                    ("normal_user", "Normal User"),
                    ("admin", "Admin"),
                ],
                default="normal_user",
                max_length=20,
            ),
        ),
    ]
