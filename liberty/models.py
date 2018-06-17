from django.db import models
import os


# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('static/photos', str(instance.id), filename)


class Author(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ПІБ')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Автора'
        verbose_name_plural = 'Автор'


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорія'


class Department(models.Model):
    title = models.CharField(max_length=200, verbose_name='Факультети')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультет'


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    lib_id = models.CharField(max_length=200, verbose_name='Номер')
    year = models.CharField(max_length=200, verbose_name='Рік')
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True,  verbose_name='Обкладинка')
    description = models.TextField(verbose_name='Опис')
    count = models.IntegerField(verbose_name='Кiлькiсть')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    book_file = models.FileField(upload_to=os.path.join('static/uploads'), default='', verbose_name='Файл книги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книжка'
        verbose_name_plural = 'Книжку'


class Student(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ПІБ')
    year_entry = models.DateTimeField(verbose_name='Рік початку навчання')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Факультет')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студента'


class BookStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    count = models.IntegerField(verbose_name='Кiлькiсть')
    get_date = models.DateTimeField(verbose_name='Отримав')
    return_date = models.DateTimeField(verbose_name='Віддав')

    def __str__(self):
        return self.student.full_name + ' повинен книгу ' + self.book.title

    class Meta:
        verbose_name = 'Борг'
        verbose_name_plural = 'Борги'