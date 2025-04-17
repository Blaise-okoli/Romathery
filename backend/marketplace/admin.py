from django.contrib import admin
from .models import Vendor, Product
from .utils import upload_image_to_supabase


class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'vendor')
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
