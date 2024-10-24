# Generated by Django 5.1.1 on 2024-10-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(blank=True, null=True, verbose_name="Контент"),
        ),
        migrations.AlterField(
            model_name="post",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Опубликовать"),
        ),
    ]
