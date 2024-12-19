"""
Definition of models.
"""

from ast import mod
from email.mime import image
from itertools import count
from math import prod
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = 'temp.jpg', verbose_name='Путь к картинке')

    # Методы экземпляра
    def get_absolute_url(self):
        # метод возвращает строку с URL-адресом записи
        return reverse('blogpost', args=[str(self.id)])

    def __str__(self):
        # метод возвращает название, используемое для представления отдельной записи в административном разделе
        return self.title

    # Метаданные – вспомогательный класс, который задает дополнительные параметры модели
    class Meta:
        db_table = 'Posts'  # имя таблицы для модели
        ordering = ["-posted"]  # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "статья блога"  # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога"  # то же для всех статей блога

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Дата комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Статья комментария')

    # Метод возвращает название, искомую дату преставления отдельных записей в администратором разделе
    def __str__(self):
        return 'Комментарий %d %s к %s' %(self.id, self.author, self.post)

    class Meta:
        db_table = 'Comment'
        ordering = ['-date']
        verbose_name = 'Комментарии к статье блога'
        verbose_name_plural = 'Комментарии к статьям блога'

admin.site.register(Comment)

class product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название продукта")
    description = models.TextField(default='', verbose_name="Описание")
    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def get_absolute_url(self):
        return reverse("product", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "товары"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('processing', 'В процессе'),
        ('shipped', 'Отправлено'),
        ('delivered', 'Доставлено'),
        ('cancelled', 'Отменено'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Заказ {self.id} от {self.user.username}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    class Meta:
        verbose_name = "Элемент заказа"
        verbose_name_plural = "Элементы заказа"

class OrderQuerySet(models.QuerySet):
    def by_user(self, user):
        return self.filter(user=user)

    def by_status(self, status):
        return self.filter(status=status)

    def recent_orders(self):
        return self.order_by('-order_date')
   
admin.site.register(product)