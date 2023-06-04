from django.db import models


# ----------------------------------------------------------------------------------------------------------------------
# Create models
class Contact(models.Model):
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street_name = models.CharField(max_length=50, verbose_name='Улица')
    building_number = models.CharField(max_length=6, null=True, blank=True, verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self) -> str:
        """Returns the email of the contact information"""
        return self.email
