import django_filters
from django.db.models import Q

from .models import Product


class ProductFilter(django_filters.FilterSet):
    # 自定义过滤字段
    q = django_filters.CharFilter(method='my_custom_filter', label='关键词')

    def my_custom_filter(self, queryset, q, value):
        # return queryset.filter(Q(PartNo__icontains=value) | Q(Description__icontains=value))
        return queryset.filter(PartNo__icontains=value)

    class Meta:
        # 使用哪个模型和哪些字段过滤
        model = Product
        fields = {
            'PartNo'
        }
