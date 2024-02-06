from rest_framework import permissions


class OwnerUser(permissions.BasePermission):
    SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.author == request.user:
            return True

        return False
    
