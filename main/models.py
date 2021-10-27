from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length= 60 )
    task = models.TextField('Описание')
    def __str__(self):
        return self.title

class FIO(models.Model):
    filter = models.CharField('имя', max_length=30)
    Surname = models.CharField('Фамилия', max_length=40)
    Otchevstvo = models.CharField('Отчество', max_length=40)
    Age = models.CharField('Возраст', max_length=40)
    def __str__(self):
        return self.filter


class Tovar(models.Model):
    title_name = models.CharField(verbose_name='Наименование', max_length=100)
    Description = models.TextField(verbose_name='Описание')
    cost = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2)
    mass = models.DecimalField(verbose_name='Масса', max_digits=5, decimal_places=0)
    imagefile = models.ImageField(upload_to='main/static/main/loadimg')
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.title_name