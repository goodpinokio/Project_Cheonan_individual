# Generated by Django 4.2.2 on 2023-06-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_post_file_upload"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="hook_text",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
