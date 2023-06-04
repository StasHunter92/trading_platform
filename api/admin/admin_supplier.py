from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from api.models.supplier_model import Supplier


# ----------------------------------------------------------------------------------------------------------------------
# Create admin models
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin settings for the supplier"""

    actions: tuple = ('clean_indebtedness',)
    list_display: tuple[str, ...] = (
        'title',
        'type',
        'supplier_link',
        'supplier_city',
        'supplier_contact',
        'indebtedness',
        'level'
    )
    list_display_links: tuple[str, ...] = ('title',)
    list_filter: tuple[str, ...] = ('supplier__contact__city',)
    filter_horizontal = ('products',)
    readonly_fields: tuple[str, ...] = ('created', 'supplier_contact', 'level')

    fieldsets: tuple[tuple[str, dict[str, tuple]], ...] = (
        ('Общая информация', {
            'fields': ('type', 'title', 'contact')
        }),
        ('Товарные операции', {
            'fields': ('products', 'supplier', 'supplier_contact', 'indebtedness')
        }),
        ('Техническая информация', {
            'fields': ('created', 'level')
        }),
    )

    @admin.display(description='Контактные данные')
    def supplier_contact(self, supplier: Supplier) -> str | None:
        """
        Returns the email address of the nested supplier model
        Args:
            supplier: Supplier object
        Returns:
            email or None if Supplier object does not have nested supplier
        """

        if supplier.supplier:
            return supplier.supplier.contact.email

        return None

    @admin.display(description='Поставщик')
    def supplier_link(self, supplier: Supplier) -> str | None:
        """
        Returns the link to the nested supplier
        Args:
            supplier: Supplier object
        Returns:
            link or None if Supplier object does not have nested supplier
        """

        if supplier.supplier:
            url = reverse('admin:api_supplier_change', args=[supplier.supplier.id])
            return format_html(f'<a href={url}>{supplier.supplier.title}</a>')

        return None

    @admin.display(description='Город отправки')
    def supplier_city(self, supplier: Supplier) -> str | None:
        """
        Returns the city of the nested supplier
        Args:
            supplier: Supplier object
        Returns:
            city or None if Supplier object does not have nested supplier
        """

        if supplier.supplier:
            return supplier.supplier.contact.city

        return None

    @admin.action(description='Очистить задолженность')
    def clean_indebtedness(self, request, queryset):
        """Admin action to clean the indebtedness"""

        queryset.update(indebtedness=None)
