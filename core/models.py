from django.contrib.auth.models import AbstractUser


# ----------------------------------------------------------------------------------------------------------------------
# Create models
class User(AbstractUser):
    """Custom User model"""

    class Meta:
        """Meta information for the user model"""
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'
