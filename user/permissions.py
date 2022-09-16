
from rest_framework.permissions import BasePermission
from django.conf import settings
from user.models import User

class IsAdmin(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user