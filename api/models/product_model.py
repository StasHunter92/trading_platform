from django.db import models


# ----------------------------------------------------------------------------------------------------------------------
# Create models
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        """Returns the title of the product"""
        return f'{self.title} {self.model}'
