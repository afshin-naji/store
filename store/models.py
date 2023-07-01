
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='نام')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='نام قابل استفاده در نوار مرورگر')

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, verbose_name='دسته بندی')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ایجاد شده توسط')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    author = models.CharField(max_length=255, default='unknown', verbose_name='نویسنده')
    short_description = models.CharField(max_length=2000, blank=True, verbose_name='خلاصه کوتاه')
    long_description = models.TextField(blank=True, verbose_name='خلاصه بلند')
    image = models.ImageField(upload_to='images/', verbose_name='تصویر جلد')
    slug = models.SlugField(max_length=255, verbose_name='نام قابل استفاده در نوار مرورگر')
    price = models.DecimalField(max_digits=10, decimal_places=3, verbose_name='قیمت')
    in_stock = models.BooleanField(default=True, verbose_name='موجود در انبار')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین تغییر')

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

