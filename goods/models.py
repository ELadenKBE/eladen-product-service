from django.core.validators import MinValueValidator
from django.db import models

from category.models import Category
from users.models import ExtendedUser


# Create your models here.
# test line

class Good(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    title = models.CharField(max_length=256)
    seller = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=5000, null=True, blank=True)
    manufacturer = models.CharField(max_length=256, null=True, blank=True)
    amount = models.IntegerField(blank=False,
                                 default=99,
                                 validators=[MinValueValidator(0)],
                                 null=True)
