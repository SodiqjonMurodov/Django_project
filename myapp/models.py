from django.db import models
from django.urls import reverse


class Categories(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category


class Fruits(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='related_name')
    price = models.FloatField()
    kg = models.IntegerField()
    image = models.ImageField(upload_to='db_images')
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Main table'

    def get_absolute_url(self):
        return reverse('main', kwargs={'raqam': self.id})

    def __str__(self):
        return self.name




