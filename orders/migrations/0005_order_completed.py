# Generated by Django 5.0.2 on 2024-04-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_alter_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]