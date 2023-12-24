from rest_framework import serializers
from ecommerce.models import ProductModel

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
       