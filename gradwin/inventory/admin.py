# from .models import Order
from django.contrib import admin
from .models import Product, Category


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'buying_price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# class CategoryAdmin(DraggableMPTTAdmin):
#     mptt_indent_field = "name"
#     list_display = ('tree_actions', 'indented_title',
#                     'related_products_count', 'related_products_cumulative_count')
#     list_display_links = ('indented_title',)

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)

#         # Add cumulative product count
#         qs = Category.objects.add_related_count(
#             qs,
#             Product,
#             'category',
#             'products_cumulative_count',
#             cumulative=True)

#         # Add non cumulative product count
#         qs = Category.objects.add_related_count(qs,
#                                                 Product,
#                                                 'category',
#                                                 'products_count',
#                                                 cumulative=False)
#         return qs

#     def related_products_count(self, instance):
#         return instance.products_count
#         related_products_count.short_description = 'Related products (for this specific category)'

#     def related_products_cumulative_count(self, instance):
#         return instance.products_cumulative_count
#         related_products_cumulative_count.short_description = 'Related products (in tree)'


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
