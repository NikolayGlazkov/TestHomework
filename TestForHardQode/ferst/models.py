from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User

class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название продукта")
    start_datetime = models.DateTimeField(verbose_name="Дата и время старта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость продукта")  
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Связь с создателем продукта")
    min_students = models.IntegerField(default=1, verbose_name="Минимальное количество студентов")  
    max_students = models.IntegerField(default=30, verbose_name="Максимальное количество студентов")

    def __str__(self):
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['user', 'product']
        
    def __str__(self):
        return f"{self.user} - {self.product}"

class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название урока")
    video_url = models.URLField(verbose_name="Ссылка на видео")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Связь с продуктом")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок урока")

    def __str__(self):
        return f"{self.title} - {self.video_url}"

class Group(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название группы")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, verbose_name="Участники")


    def __str__(self):
        return f"{self.name}"
