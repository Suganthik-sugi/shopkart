from django.contrib import admin
from .models import Catagory
from .models import Product
# class CategoryAdmin(admin.ModelAdmin):
    # list_display=('name','image','description')
# admin.site.register(Catagory,CategoryAdmin)

# Register your models here.
admin.site.register(Catagory)
admin.site.register(Product)