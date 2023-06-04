from django.contrib import admin

from api.models.product_model import Product


# ----------------------------------------------------------------------------------------------------------------------
# Create admin models
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin settings for the product"""

    list_display: tuple[str, ...] = (
        'title',
        'model',
        'release_date'
    )

    fieldsets: tuple[tuple[str, dict[str, tuple]], ...] = (
        ('Техническая информация', {
            'fields': ('title', 'model', 'release_date')
        }),
    )
