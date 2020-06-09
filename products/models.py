from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# Create your models here.

# Category model
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


class Category(MPTTModel):
    STATUS = (
        ('True','True'),
        ('False','False'),
    )

    parent = TreeForeignKey('self',blank=True,null = True,related_name='children',on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank='default.jpg',upload_to='images/')
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField(null=False,unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return '/'.join(full_path[::-1])

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # many to one relation with category
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    amount = models.IntegerField()
    minamount = models.IntegerField()
    image = models.ImageField(default='default.jpg',upload_to='images/')
    detail = RichTextUploadingField()
    status = models.CharField(max_length=50,choices=STATUS)
    slug = models.SlugField(null=False,unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('prod_detail',kwargs={'slug':self.slug})

# to create read only image filed
    def image_tag(self):
        return mark_safe('<img src="{}" height=50/>'.format(self.image.url))


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

        # to create read only image filed
    def image_tag(self):
        return mark_safe('<img src="{}" height=50/>'.format(self.image.url))


# category back up database
#######################################
# class Category(models.Model):
#     STATUS = (
#         ('True','True'),
#         ('False','False'),
#     )
#
#     parent = models.ForeignKey('self',blank=True,null = True,related_name='children',on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     keywords = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     image = models.ImageField(blank='default.jpg',upload_to='images/')
#     status = models.CharField(max_length=10,choices=STATUS)
#     slug = models.SlugField()
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title
###############################################