from rest_framework import permissions
from users.models import  User
from rest_framework.views import View
import ipdb

class IsEmployee(permissions.BasePermission):
     def has_object_permission(self, request, view: View, obj:User) -> bool:
          print(request)
         
          if request.user.is_superuser:
               
               return True
          else: 
            return False