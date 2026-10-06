from django.db import models
from datetime import date

class HomePageInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис факультету")
    contacts = models.TextField(verbose_name="Контакти", blank=True, null=True)

    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=275, verbose_name="Назва кафедри")
    head_name = models.CharField(max_length=275, verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=240, verbose_name="ПІБ викладача")
    teacher_role = models.CharField(max_length=200, verbose_name="Посада викладача")
    academic_degree = models.CharField(max_length=200, verbose_name="Наукова ступінь", blank=True, null=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="teachers")

    def __str__(self):
        return self.teacher_name

class Program(models.Model):
    pr_name = models.CharField(max_length=240, verbose_name="Назва спеціальності")
    pr_code = models.CharField(max_length=3, verbose_name="Код спеціальності")
    coordinator_name = models.CharField(max_length=100, verbose_name="ПІБ координатора")
    coordinator_contacts = models.CharField(max_length=150, verbose_name="Контакти координатора")
    disciplines = models.TextField(verbose_name="Список дисциплін")
    course_description = models.TextField(verbose_name="Опис спеціальності")

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs")

    def __str__(self):
        return self.pr_name

class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255, verbose_name="Університет")
    country = models.CharField(max_length=100, verbose_name="Країна", default="")
    languages = models.CharField(max_length=150, verbose_name="Мови навчання")
    places = models.IntegerField(verbose_name="Кількість місць")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")

    def __str__(self):
        return self.university

    @property
    def is_active(self):
        return self.deadline >= date.today()
