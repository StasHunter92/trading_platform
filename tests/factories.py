import factory
from django.contrib.auth import get_user_model

from api.models.contact_model import Contact
from api.models.product_model import Product
from api.models.supplier_model import Supplier

# ----------------------------------------------------------------------------------------------------------------------
# Get user model from project
User = get_user_model()


# ----------------------------------------------------------------------------------------------------------------------
# Create factories
class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating User instances with randomized data
    Returns:
        User instance with randomized data
    """

    username = factory.Faker("user_name")
    password = factory.Faker("password")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    class Meta:
        model = User

    @classmethod
    def create(cls, **kwargs):
        custom_password = kwargs.pop("password", None)
        user = super().create(**kwargs)
        if custom_password:
            user.set_password(custom_password)
            user.save()
        else:
            user.set_password(str(cls.password))
            user.save()
        return user


# ----------------------------------------------------------------
class SupplierFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Supplier instances with randomized data
    Returns:
        Supplier instance with randomized data
    """

    title = factory.Faker("company")

    class Meta:
        model = Supplier


# ----------------------------------------------------------------
class ContactFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Contact instances with randomized data
    Returns:
        Contact instance with randomized data
    """

    email = factory.Faker("company_email")
    country = factory.Faker("country")
    city = factory.Faker("city")
    street_name = factory.Faker("street_name")
    building_number = factory.Faker("building_number")

    class Meta:
        model = Contact


# ----------------------------------------------------------------
class ProductFactory(factory.django.DjangoModelFactory):
    """
    Factory for creating Product instances with randomized data
    Returns:
        Product instance with randomized data
    """

    title = factory.Faker("catch_phrase")
    model = factory.Faker("building_number")
    release_date = factory.Faker("date", pattern="%Y-%m-%d")

    class Meta:
        model = Product
