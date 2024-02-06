from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import ResgistrationSerializer


@api_view(['POST', ])
def registration_view(request):

    if request.method == 'POST':
        serializer = ResgistrationSerializer(data=request.data)
        data = {} 

        if serializer.is_valid():
            account = serializer.save() 
            
            data["response"] = "Succesful Registered" 
            data["username"] = account.username 
            data["email"] = account.email 

            #token = Token.objects.get(user=account).key
            #data["token"] = token 

            refresh_token = RefreshToken.for_user(account)
            data["token"] = {
                "refresh":str(refresh_token),
                "access":str(refresh_token.access_token)
            }
            
        else:
            data = serializer.errors 

        return Response(data) 
    
# LogOut-View
@api_view(["POST",])
def logout_view(request):

    if request.method == "POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# Registration View - For the Profile
@api_view(['POST', ])
def user_profile_registration_view(request):

    if request.method == 'POST':
        serializer = ResgistrationSerializer(data=request.data)
        data = {} 

        if serializer.is_valid():
            account = serializer.save() 
            
            data["response"] = "Succesful Registered" 
            data["username"] = account.username 
            data["email"] = account.email 

            token = Token.objects.get(user=account).key
            data["token"] = token 
            
        else:
            data = serializer.errors 

        return Response(data) 

    
        