from django.db import models

# Create your models here.
class Tovar(models.Model):
    title = models.CharField('Название', max_length=30)
    count = models.IntegerField('Количество')
    gabarit = models.CharField('Габариты', max_length=20)
    price = models.IntegerField('Цена')
    image = models.ImageField('Изображение', upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    #gabarit = models.CharField('Габариты', max_length=20)
    #price = models.IntegerField('Цена')
    #image = models.ImageField('Изображение', upload_to='images/')
    name = models.CharField('ФИО', max_length=75)
    phone = models.CharField('Телефон', max_length=20)
    address = models.CharField('Адрес', max_length=75)
    email = models.CharField('email', max_length=50)
    tovarid = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    tovarname = models.CharField('Название товара', max_length=50)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'