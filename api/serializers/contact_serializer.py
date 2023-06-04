from rest_framework import serializers

from api.models.contact_model import Contact


# ----------------------------------------------------------------------------------------------------------------------
# Create serializers
class ContactSerializer(serializers.ModelSerializer):
    """CRUD serializer for the contact"""

    class Meta:
        model = Contact
        exclude: tuple = ('id',)
