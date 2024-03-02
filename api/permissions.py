from rest_framework import permissions
from django.contrib.auth.models import User
from user_app.models import UserModelAPI

class IsOwnerOrReadOnly(permissions.BasePermission):
    SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True 
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
                
        if obj.owner == request.user:
            return True

        return False
