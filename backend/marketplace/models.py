from django.db import models
import os
from .utils import upload_image_to_supabase

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_file = models.FileField(upload_to="temp/", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # If a new image is uploaded via the admin
        if self.image_file:
            # Upload to Supabase
            public_url = upload_image_to_supabase(self.image_file, self.image_file.name)
            if public_url:
                self.image_url = public_url

            # Remove the temp file from local storage
            file_path = self.image_file.path
            if os.path.exists(file_path):
                os.remove(file_path)

            # Clear the local file field
            self.image_file = None
            

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name