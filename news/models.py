from audioop import reverse

from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User



class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)
    description = models.TextField('Текст', null=True)
    author = models.CharField('Имя автора', max_length=100, null=True)
    date = models.DateField('Дата публикации', null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Userform2(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



