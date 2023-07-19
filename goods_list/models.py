from django.db import models

from goods.models import Good
from users.models import ExtendedUser


class GoodsList(models.Model):
    title = models.CharField(max_length=256, blank=False)
    user_id = models.IntegerField(max_length=100)
    goods = models.ManyToManyField(Good)
