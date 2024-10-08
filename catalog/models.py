from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="photos/", blank=True, null=True, verbose_name="Изображение"
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Категория",
        help_text="Введите наименование категории",
    )
    price = models.FloatField(
        verbose_name="Цена за покупку",
        help_text="Введите цену за покупку",
        null=True,
        blank=True,
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите категорию продукта"
    )
    description = models.TextField(null=True, blank=True)
    group = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="catalog")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]
