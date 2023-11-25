# Generated by Django 4.2.7 on 2023-11-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(verbose_name='Текст')),
                ('author', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]