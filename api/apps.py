from django.apps import AppConfig


# ----------------------------------------------------------------------------------------------------------------------
# Create configuration
class ApiConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'api'
