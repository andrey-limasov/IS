from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dbname = models.CharField(max_length=100)
    dbuser = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)

    class Meta:
        # …
        permissions = (("can_see_db", "Can see db settings"),)