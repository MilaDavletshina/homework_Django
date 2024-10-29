from django.db import models

from users.models import User


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
    unpublish = models.BooleanField(default=False, verbose_name="Статус публикации")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        help_text='Укажите пользователя продукта',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
        ]
        permissions = [
            ('can_unpublish_product', 'can unpublish product'),
            ('can_delete_product', 'can delete product'),
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
