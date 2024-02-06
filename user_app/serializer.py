from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ValidationError, CharField
from django.http import Http404
from rest_framework.response import Response

from .models import UserProfile

class ResgistrationSerializer(ModelSerializer):
    password2 = CharField(
        style = {"input_type":"password"}, write_only = True
    )

    class Meta():
        model = User
        fields = ["username","email", "password", "password2"]
        extra_kwargs = {
            "password":{"write_only":True}
        }
    
    def save(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        if password != password2:
            raise ValidationError({"error":"password and password2 do not match"})
        
        email = self.validated_data["email"]
        username = self.validated_data["username"]

        if User.objects.filter(email=email).exists():
            account = User(email=email, username=username)
            #account.set_password(password)
            return account
        
        account = User(email=email, username=username)
        account.set_password(password)
        account.save()

        return account
    

