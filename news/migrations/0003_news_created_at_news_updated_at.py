# Generated by Django 5.0.2 on 2024-03-14 10:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_news_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="news",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]