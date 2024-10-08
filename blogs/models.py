from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент", null=True, blank=True)
    preview = models.ImageField(
        upload_to="photos/blogs/", blank=True, null=True, verbose_name="Изображение"
    )
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")
    views_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = [
            "title",
        ]
