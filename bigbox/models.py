from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    slug = models.SlugField(verbose_name="slug")
    order = models.IntegerField(default=0, verbose_name='orden')

    class Meta:
        abstract = True
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Reason(CommonInfo):
    class Meta:
        verbose_name = "ocasión"
        verbose_name_plural = "ocasiones"
    
class Category(CommonInfo):    
    description = models.TextField(verbose_name='descripción')
    
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    internal_name = models.CharField(max_length=200, verbose_name='nombre interno')
    description = models.TextField(verbose_name='descripción')
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='categorías')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Activity(Product):
    reasons = models.ManyToManyField(Reason, blank=True, verbose_name='ocasiones')
    purchase_available = models.BooleanField(default=False, verbose_name='disponible venta individual')

    class Meta:
        verbose_name = "experiencia"
        verbose_name_plural = "experiencias"

class Box(Product):
    activities = models.ManyToManyField(Activity, verbose_name="experiencias")
    price = models.IntegerField(verbose_name='precio de venta')
    purchase_available = models.BooleanField(default=False, verbose_name='disponible venta individual')
    slug = models.CharField(blank=True, max_length=200, null=True, verbose_name="slug")

    class Meta:
        verbose_name = "box"
        verbose_name_plural = "boxes"