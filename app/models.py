from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Doctor(AbstractUser):
    experience = models.IntegerField(null=True, blank=True, default=0)
    description = models.CharField(max_length=255, null=True, blank=True)
    contacts = models.IntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, default="avatars/default_user.png")
    department = models.ManyToManyField(Department)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.department}"
