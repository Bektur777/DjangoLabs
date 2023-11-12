from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class CustomerCL(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('customer', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class TagCL(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        data = [
            TagCL(name='S'),
            TagCL(name='M'),
            TagCL(name='L'),
            TagCL(name='XL')
        ]
        TagCL.objects.bulk_create(data)


class ProductCL(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class OrderCL(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductCL)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Order #{self.pk} - {self.user} - {self.order_date}"

    def get_absolute_url(self):
        return reverse('order', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
