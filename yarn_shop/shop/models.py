from django.db import models

# Create your models here.
from django.urls import reverse


class Producer(models.Model):
    prod = models.CharField(max_length=200, verbose_name='Producer')

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'

    def __str__(self):
        return self.prod


class Country(models.Model):
    count = models.CharField(max_length=12, verbose_name='Country')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.count


class Category(models.Model):
    cat = models.CharField(max_length=30, verbose_name='Category')
    url = models.SlugField(unique=True, verbose_name='Url')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.cat

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.url})


class SubCategory(models.Model):
    name = models.CharField(max_length=40, verbose_name='Name')
    url = models.SlugField(unique=True, verbose_name='Url')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='subcategory/', blank=True, verbose_name='Image')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category', verbose_name='Category')
    count = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='country',  verbose_name='Country')
    prod = models.ForeignKey(Producer, on_delete=models.PROTECT, related_name='producer',  verbose_name='Producer')
    price = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='Price')
    weight = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='Weight')
    length = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name='Length')
    spokes = models.CharField(max_length=10, blank=True,  verbose_name='Spokes')
    hook = models.CharField(max_length=10, blank=True,  verbose_name='Hook')
    material = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcat', kwargs={'subcat_slug': self.url})


class YarnImages(models.Model):
    title = models.CharField(max_length=40,  verbose_name='Name')
    image = models.ImageField(upload_to='yarnimages/',  verbose_name='Image')
    subcat = models.ForeignKey(SubCategory, on_delete=models.PROTECT,  verbose_name='SubCategory',)

    class Meta:
        verbose_name = 'YarnImage'
        verbose_name_plural = 'YarnImages'

    def __str__(self):
        return self.title


class Color(models.Model):
    col = models.CharField(max_length=30,  verbose_name='Color')

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.col


class Yarn(models.Model):
    name = models.CharField(max_length=40,  verbose_name='Name')
    url = models.SlugField(unique=True,  verbose_name='Url')
    image = models.ImageField(upload_to='yarn/',  verbose_name='Image')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT,  verbose_name='Category')
    count = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Country')
    prod = models.ForeignKey(Producer, on_delete=models.PROTECT, verbose_name='Producer')
    subcat = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='subcategory_yarns',  verbose_name='SubCategory', )
    col = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='color',  verbose_name='Color')
    time_add = models.DateTimeField(auto_now_add=True,  verbose_name='Time_add')
    time_update = models.DateTimeField(auto_now=True,  verbose_name='Time_update')
    availability = models.BooleanField(default=True,  verbose_name='Availability')

    class Meta:
        verbose_name = 'Yarn'
        verbose_name_plural = 'Yarns'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.url})






