from django.db import models

# Create your models here.

class Websta(models.Model):
    writer = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
