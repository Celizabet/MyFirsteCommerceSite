from rest_framework import serializers
from ecommerce.models import ProductModel
from forms.models import UserClientModel
from django.contrib.auth.models import User
#from user_app.models import UserModelAPI

class ApiSerializer(serializers.ModelSerializer):
    """Serializa un campo de nombre para nuestra APIView"""
    class Meta():
        model = ProductModel
        fields = [
            "title",
            "price",
            "description",
            "seller",
            "color",
            "product_dimensions",
            "slug",
            "user"
        ]


class UserModelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta():
        model = User
        fields = [
            "owner",
            "username",          
            "email",
            "password",
            "eCommerceStore"
        ]

