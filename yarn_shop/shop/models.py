from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=30)
    url = models.SlugField(unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Color(models.Model):
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Producer(models.Model):
    producer = models.CharField(max_length=200)

    def __str__(self):
        return self.producer

    class Meta:
        verbose_name = 'Producer'
        verbose_name_plural = 'Producers'


class Yarn(models.Model):
    name = models.CharField(max_length=50)
    url = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='shop/')
    price = models.SmallIntegerField()
    length = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    needles = models.CharField(max_length=50)
    hook = models.CharField(max_length=50)
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT, related_name='producer_name')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='color_name')
    yarn_add = models.DateTimeField(auto_now=True)
    yarn_update = models.DateTimeField(auto_now_add=True)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Yarn'
        verbose_name_plural = 'Yarns'


class YarnImages(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='shop/')
    yarn = models.ForeignKey(Yarn, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'YarnImage'
        verbose_name_plural = 'YarnImages'


