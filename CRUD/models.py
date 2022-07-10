from django.db import models


class Main(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    desc = models.TextField()
    created = models.DateField(auto_now=True)





