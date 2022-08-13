from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название проекта')
    url = models.URLField(verbose_name='Ссылка на проект', **NULLABLE)
    description = models.CharField(max_length=255, verbose_name='Описание проекта')
    image = models.ImageField(upload_to='portfolio/images/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at', 'title']

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def __str__(self):
        return f'{self.title} {self.created_at}'
