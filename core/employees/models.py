from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from tags.models import Tag


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='DefaultFirstName')
    last_name = models.CharField(max_length=100, default='DefaultLastName')
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, default='NotSpecified')
    date_of_birth = models.DateField(default='2000-01-01')
    address = models.CharField(max_length=255, default='DefaultAddress')
    country = models.CharField(max_length=100, default='DefaultCountry')
    province = models.CharField(max_length=100, default='DefaultProvince')
    city = models.CharField(max_length=100, default='DefaultCity')
    area_code = models.CharField(max_length=10, default='0000')
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
