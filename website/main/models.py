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