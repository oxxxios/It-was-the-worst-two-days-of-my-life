from django.db import models
from colorfield.fields import ColorField
from users.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=255, verbose_name="Категория")
    is_popular = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.category_name



class Product(models.Model):
    image = models.ImageField(upload_to="media/", verbose_name="Фото товара")
    title = models.CharField(max_length=255, verbose_name="Название товара")
    subtext = models.TextField(max_length=200, verbose_name="Подтекст")
    price = models.PositiveIntegerField(verbose_name="Цена")
    color = ColorField(default="#E224A3", verbose_name="Цвет")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория товара", related_name="product")

    @property
    def rating(self):
        return self.reviews.aggregate(avg_rating=models.Avg('stars'))['avg_rating']

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст")
    rate = models.IntegerField(verbose_name="Оценка", choices=([i, i * "*"] for i in range(1, 6)))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Отзыв к товару", related_name="reviews")


    def __str__(self) -> str:
        return f'{self.author}-{self.product.title}'