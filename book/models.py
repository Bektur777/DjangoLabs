from django.db import models
from django.urls import reverse


# Create your models here.


class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=255)
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(verbose_name='Картинка', upload_to='')
    cost = models.SmallIntegerField(verbose_name='Цена книги')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
