from django.contrib import admin

from api.models.contact_model import Contact


# ----------------------------------------------------------------------------------------------------------------------
# Create admin models
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin settings for the contact"""

    list_display: tuple[str, ...] = (
        'email',
        'country',
        'city',
        'street_name',
        'building_number'
    )
    list_filter: tuple[str, ...] = ('city',)

    fieldsets: tuple[tuple[str, dict[str, tuple]], ...] = (
        ('Контактные данные', {
            'fields': ('email',)
        }),
        ('Адрес', {
            'fields': ('country', 'city', 'street_name', 'building_number')
        }),
    )
