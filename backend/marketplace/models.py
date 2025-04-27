from django.db import models
import os
from .utils import upload_image_to_supabase

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="vendors")

    def __str__(self):
        return self.name
    
class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_file = models.FileField(upload_to="temp/", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id'] # newest products first (descending)