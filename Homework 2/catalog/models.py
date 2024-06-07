from django.db import models

NULLABLE = {"blank": True, "null": True}

from users.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Добавьте описание категории",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Добавьте описание продукта",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="catalog/images",
        verbose_name="Превью",
        help_text="Загрузите изображение товара",
        **NULLABLE,
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        **NULLABLE,
        related_name="products",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        help_text="Добавьте цену продукта",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(verbose_name="Дата изменения", **NULLABLE)

    owner = models.ForeignKey(
        User, verbose_name="Кем создан",
        help_text="Укажите кем создан продукт",
        **NULLABLE,
        on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at", "updated_at"]

    def __str__(self):
        return f"{self.name}"


class BlogPost(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.CharField(
        max_length=150,
        verbose_name="Слаг",
        help_text="Добавьте слаг",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Добавьте содержимое",
    )
    preview = models.ImageField(
        upload_to="blog/images",
        verbose_name="Превью",
        help_text="Загрузите изображение",
        **NULLABLE,
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Добавьте дату создания",
    )
    is_published = models.BooleanField(
        verbose_name="Опубликовано?",
        help_text="Опубликовать запись",
        default=False,
    )
    views_count = models.IntegerField(
        verbose_name="Количество просмотров",
        help_text="Добавьте количество просмотров",
        default=0,
        **NULLABLE,
    )


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="version",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="версия продукта",
        help_text="Введите версию продукта",
    )
    number = models.PositiveIntegerField(
        verbose_name="Номер версии", help_text="Введите номер версии"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    is_active = models.BooleanField(
        verbose_name="Активная версия?",
        help_text="Отметьте активность версии",
        default=False,
    )

    def __str__(self):
        return f"{self.product}. Версия №{self.number}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
