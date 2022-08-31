from django.db import models
from portfolioapp.models import NULLABLE


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


class Blog(BaseModel):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст поста')
    image = models.ImageField(upload_to='portfolio/images/', **NULLABLE)

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
        ordering = ['-created_at', 'title']

    def __str__(self):
        return f'{self.title} {self.created_at}'
