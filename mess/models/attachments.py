from django.db import models


class Images(models.Model):
    """Модель изображений, прикрепляемых к Mess"""

    link = models.TextField(verbose_name='Link')  # Ссылка на файл в файловой системе
    name = models.CharField(verbose_name='Name', max_length=255)  # Название файла
    weight = models.IntegerField(verbose_name='Weight')  # Размер изображения в байтах
    created_date = models.DateTimeField(verbose_name='Date', auto_now=True)  # Дата добавления
    order = models.PositiveSmallIntegerField(verbose_name='Order')  # Порядок добавления

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.name


class Videos(models.Model):
    """Модель видео, прикрепляемых к Mess"""

    link = models.TextField(verbose_name='Link')  # Ссылка на файл в файловой системе или в сети
    name = models.CharField(verbose_name='Name', max_length=255)  # Название файла
    weight = models.BigIntegerField(verbose_name='Weight')  # Размер видео в байтах
    created_date = models.DateTimeField(verbose_name='Date', auto_now=True)  # Дата добавления
    order = models.PositiveSmallIntegerField(verbose_name='Order')  # Порядок добавления

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.name


class Audios(models.Model):
    """Модель аудио, прикрепляемых к Mess"""

    link = models.TextField(verbose_name='Link')  # Ссылка на файл в файловой системе или в сети
    name = models.CharField(verbose_name='Name', max_length=255)  # Название файла
    weight = models.BigIntegerField(verbose_name='Weight')  # Размер аудио в байтах
    created_date = models.DateTimeField(verbose_name='Date', auto_now=True)  # Дата добавления
    order = models.PositiveSmallIntegerField(verbose_name='Order')  # Порядок добавления

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'

    def __str__(self):
        return self.name


class Files(models.Model):
    """Модель файлов, прикрепляемых к Mess"""

    link = models.TextField(verbose_name='Link')  # Ссылка на файл в файловой системе
    name = models.CharField(verbose_name='Name', max_length=255)  # Название файла
    weight = models.BigIntegerField(verbose_name='Weight')  # Размер файла в байтах
    created_date = models.DateTimeField(verbose_name='Date', auto_now=True)  # Дата добавления
    order = models.PositiveSmallIntegerField(verbose_name='Order')  # Порядок добавления

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.name
