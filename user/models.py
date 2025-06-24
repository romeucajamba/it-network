from django.db import models

# Create your models here.

class User(models.Model):
   name = models.CharField(max_length=100, null=False, default="")
   email = models.EmailField(max_length=100, unique=True, null=False, default="")
   password = models.CharField(max_length=100, null=False, default="")

   def __str__(self):
      return f"{self.name} - {self.email}"