from django.db import models
from django.urls import reverse

class Buyer(models.Model):                      # первая таблица для базы данных
    name = models.CharField(max_length=50, db_index=True, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Почта')
    phona_namber = models.CharField(max_length=20, blank=True, null=True, verbose_name='Телефон')
    age = models.IntegerField(verbose_name='Bозраст пользователя')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.name



class Person1(models.Model):            # вторая таблица для базы данных сначала создана в базе данных и затем прописана в python
    product = models.TextField(max_length=20, db_index=True, verbose_name='продукт')
    prise = models.IntegerField(verbose_name='цена')

    def __str__(self):
        return self.product




class Animals_in_the_zoo(models.Model):         # третья таблица создана сначала в базе данных и затем прописана в python
    name = models.TextField(max_length=15, db_index=True, verbose_name='название животного')
    animal_feed_kg_1day = models.IntegerField(verbose_name='количество корма на 1 день в кг')

    def __str__(self):
        return self.name















# Create your models here.
