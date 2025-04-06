from django.contrib import admin
from .models import Vendor, Product

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)