# Generated by Django 4.2.2 on 2024-11-04 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name"],
                "permissions": [("can_unpublish_product", "can unpublish product")],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.RemoveField(
            model_name="category",
            name="group",
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                help_text="Введите наименование категории",
                max_length=100,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="publication_status",
            field=models.BooleanField(default=False, verbose_name="Опубликовано"),
        ),
    ]
