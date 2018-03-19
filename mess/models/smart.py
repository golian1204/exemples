from django.db import models


class Category(models.Model):
    name = models.CharField('Группа товара', max_length=64)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Группа')
    name = models.CharField('Название товара', max_length=128)
    price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
