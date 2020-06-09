from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from products.models import Category, Product ,Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['parent', 'status']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

admin.site.register(Category, CategoryAdmin2)

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 7

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'status','image_tag']
    list_filter = ['category', 'status']
    readonly_fields = ['image_tag']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Product,ProductAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['product','title','image_tag']
    list_filter = ['product']
    readonly_fields = ['image_tag']

admin.site.register(Images,ImagesAdmin)