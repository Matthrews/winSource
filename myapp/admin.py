from django.contrib import admin

# Register your models here.
from .models import Product

# 应用的admin.py文件中
admin.site.site_header = 'Attcomp 电子器件网'
admin.site.site_title = 'Attcomp 电子器件网'
admin.site.index_title = u'Attcomp 电子器件网'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['PartNo', 'Manufacture', 'LowestPrice', 'CustomizePrice', 'Description', 'Availability', 'MOQ']
    list_filter = ['PartNo', 'Manufacture', 'CustomizePrice', 'Description', 'Availability']
    search_fields = ('PartNo', 'Manufacture')  # 搜索字段
    list_editable = ('CustomizePrice', 'MOQ')
    readonly_fields = ('PartNo',)


admin.site.register(Product, ProductAdmin)
