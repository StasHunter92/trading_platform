from django.contrib import admin

from core.models import User


# ----------------------------------------------------------------------------------------------------------------------
# Create admin models
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin settings for the user"""

    list_display: tuple[str, ...] = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter: tuple[str, ...] = ('is_active',)
    readonly_fields: tuple[str, ...] = ('date_joined', 'last_login')

    fieldsets: tuple[tuple[str, dict[str, tuple]], ...] = (
        ('Общая информация', {
            'fields': ('username', ('last_login', 'date_joined'))
        }),
        ('Контактная информация', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Статусная информация', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Права доступа', {
            'fields': ('groups', 'user_permissions')
        }),
    )
