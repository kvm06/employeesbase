from django.db import models

# Create your models here.
gender_choices = [
    ('man', 'Мужчина'),
    ('woman', 'Женщина')
]


class Employee(models.Model):
    """Модель сотрудника компании"""
    first_name = models.CharField(max_length=255, verbose_name='Имя', null=False, blank=False)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', null=False, blank=False)
    age = models.IntegerField(verbose_name='Возраст')
    gender = models.CharField(max_length=10, verbose_name="Пол", choices=gender_choices, null=False, blank=False)
    department = models.ForeignKey('Department', verbose_name='Отдел', on_delete=models.CASCADE)
    prog_language = models.ForeignKey('ProgrammingLanguage', verbose_name='Язык программирования', null=True,
                                      on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Department(models.Model):
    """Модель отдела компании"""
    department_name = models.CharField(max_length=255, verbose_name='Название отдела', null=False, blank=False)
    floor = models.IntegerField(verbose_name='Этаж')

    class Meta:
        verbose_name= 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.department_name


class Programminglanguage(models.Model):
    """Модель языка программирования"""
    language = models.CharField(max_length=50, verbose_name='Язык программирования', null=False, blank=False)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программрования'

    def __str__(self):
        return self.language

