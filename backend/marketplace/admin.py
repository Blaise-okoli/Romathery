from django.contrib import admin
from .models import Vendor, Product, Warehouse
from .utils import upload_image_to_supabase


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location")

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "warehouse")
    list_filter = ("warehouse",) # This adds the warehouse filter

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor')
    list_filter = ("vendor",)
    readonly_fields = ("image_url",)

    def save_model(self, request, obj, form, change):
        # Only upload if a new file was uploaded
        if form.cleaned_data.get("image_file"):
            public_url = upload_image_to_supabase(obj.image_file, obj.image_file.name)
            if public_url:
                obj.image_url = public_url
                obj.image_file = None # clear temp file if desired

        super().save_model(request, obj, form, change)


admin.site.register(Vendor, VendorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
