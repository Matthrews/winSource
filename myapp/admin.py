from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['PartNo', 'Manufacture', 'Catalog', 'Description', 'RohsLink', 'ProductionPDFLink', 'Availability',
                    'MOQ']
    list_filter =['PartNo', 'Manufacture', 'Catalog', 'Description', 'RohsLink', 'ProductionPDFLink', 'Availability',
                    'MOQ']


admin.site.register(Product, ProductAdmin)
