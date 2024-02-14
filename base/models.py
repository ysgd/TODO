from django.db import models

# Create your models here.
class todo(models.Model):
  tasks = models.CharField(max_length=50)
  description = models.TextField()
  status = models.CharField(max_length=10)