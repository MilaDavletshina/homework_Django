# Generated by Django 4.2.2 on 2024-10-25 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="tg_name",
        ),
    ]