from django.apps import AppConfig


# ----------------------------------------------------------------------------------------------------------------------
# Create configuration
class CoreConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'core'
