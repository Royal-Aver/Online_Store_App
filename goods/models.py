from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    class Meta:
        db_table = "category"
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    price = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.0, verbose_name="Цена"
    )
    discount = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Скидка"
    )
    description = models.TextField(verbose_name="Описание")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    image = models.ImageField(
        upload_to="products_images", blank=True, verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title
