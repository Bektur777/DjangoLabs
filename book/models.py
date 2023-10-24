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
        return reverse('detail_book', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class ReviewBook(models.Model):
    STARS = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),

    )
    title_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review_object')
    text_review = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=STARS)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.title_book}"

    def get_absolute_url(self):
        return reverse('review_book', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'
