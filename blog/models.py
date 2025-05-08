from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Пост")
    image = models.ImageField("Превью", upload_to="blog/", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=False)
    views_count = models.PositiveIntegerField("Просмотры", default=0)

    class Meta:
        verbose_name = "Блог-пост"
        verbose_name_plural = "Блог-посты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
