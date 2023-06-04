from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from api.models.supplier_model import Supplier
from api.serializers.contact_serializer import ContactSerializer
from api.serializers.product_serializer import ProductSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Create serializers
class NestedSupplierSerializer(serializers.ModelSerializer):
    """Serializer for the nested supplier"""

    supplier = SerializerMethodField()
    products = ProductSerializer(many=True)
    type = SerializerMethodField()

    class Meta:
        model = Supplier
        fields: tuple = ('type', 'title', 'products', 'supplier', 'level')

    def get_supplier(self, instance) -> dict | None:
        """Recursive function for the nested supplier"""

        if instance.supplier:
            return NestedSupplierSerializer(instance.supplier).data

        return None

    def get_type(self, instance) -> str:
        """Returns string representation of the type"""

        return instance.get_type_display()


# -----------------------------------------------------------------------------
class SupplierSerializer(serializers.ModelSerializer):
    """Serializer for retrieving/deleting supplier"""

    supplier = NestedSupplierSerializer()
    products = ProductSerializer(many=True)
    contact = ContactSerializer()
    type = SerializerMethodField()

    class Meta:
        model = Supplier
        fields: tuple = ('type', 'title', 'contact', 'products', 'supplier', 'indebtedness', 'level')

    def get_type(self, instance) -> str:
        """Returns string representation of the type"""

        return instance.get_type_display()


# -----------------------------------------------------------------------------
class SupplierCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating supplier"""

    class Meta:
        model = Supplier
        fields: str = '__all__'
        read_only_fields: tuple = ('level',)

    def validate(self, validated_data: dict) -> dict:
        """
        Checks that the Factory supplier can't have a nested supplier
        Args:
            validated_data: The validated data from the serializer
        Returns:
            The cleaned validated data
        Raises:
            serializers.ValidationError: If supplier is factory type and have nested_supplier
        """

        supplier_type: int = validated_data.get('type')
        nested_supplier = validated_data.get('supplier')

        if supplier_type == 1 and nested_supplier is not None:
            raise serializers.ValidationError('Factory does not have a supplier')

        return validated_data


# -----------------------------------------------------------------------------
class SupplierUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating supplier"""

    class Meta:
        model = Supplier
        fields: tuple = ('type', 'title', 'contact', 'products', 'supplier', 'indebtedness', 'level')
        read_only_fields: tuple = ('indebtedness', 'level')

    def validate(self, validated_data: dict) -> dict:
        """
        Checks that the Factory supplier can't have a nested supplier
        Args:
            validated_data: The validated data from the serializer
        Returns:
            The cleaned validated data
        Raises:
            serializers.ValidationError: If supplier is factory type and have nested_supplier
        """

        supplier_type: int = validated_data.get('type')
        nested_supplier = validated_data.get('supplier')

        if supplier_type == 1 and nested_supplier is not None:
            raise serializers.ValidationError('Factory does not have a supplier')

        return validated_data
