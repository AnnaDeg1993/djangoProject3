from django.db import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField('Текст')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

