from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Текст поста')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title