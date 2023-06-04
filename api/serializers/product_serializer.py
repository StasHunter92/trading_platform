from rest_framework import serializers

from api.models.product_model import Product


# ----------------------------------------------------------------------------------------------------------------------
# Create serializers
class ProductSerializer(serializers.ModelSerializer):
    """CRUD serializer for the product"""

    class Meta:
        model = Product
        exclude: tuple = ('id',)
