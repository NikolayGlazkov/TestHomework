from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User

#продукт обучения например: курс пайтон разроботчик, или python bakend:
class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название продукта")
    start_datetime = models.DateTimeField(verbose_name="Дата и время старта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость продукта")  
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Связь с создателем продукта")
    min_students = models.IntegerField(default=1, verbose_name="Минимальное количество студентов")  
    max_students = models.IntegerField(default=30, verbose_name="Максимальное количество студентов")

    def __str__(self):
        return self.name

#доступ к продукту связ один ко многим между пользователем и продуктом
class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    class Meta:
        unique_together = ['user', 'product']

    def __str__(self):
        return f"{self.user} - {self.product}"
#ссылки на урок 
class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название урока")
    video_url = models.URLField(verbose_name="Ссылка на видео")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Связь с продуктом")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок урока")

    def __str__(self):
        return f"{self.title} - {self.video_url}"
#группы например группа 1, группа 2
class Group(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название группы")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, verbose_name="Участники")


    def __str__(self):
        return f"{self.name}"
    
    def distribute_users(self):
    # Получаем количество участников в группе
        current_members_count = self.members.count()

        # Получаем минимальное и максимальное количество участников в группе
        min_members = self.product.min_students
        max_members = self.product.max_students

        # Распределяем участников в группе, если необходимо
        if current_members_count < min_members:
            available_slots = min_members - current_members_count

            # Получаем пользователей, которые не состоят в группе
            users_without_group = User.objects.exclude(groups__in=[self])

            # Определяем количество пользователей, которое добавим в группу
            users_to_add_count = min(available_slots, users_without_group.count(), max_members - current_members_count)

            # Получаем первых N пользователей, которых можно добавить
            users_to_add = users_without_group[:users_to_add_count]

            # Добавляем пользователей в группу
            self.members.add(*users_to_add)

