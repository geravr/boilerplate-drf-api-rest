# Rest Framework
from rest_framework.permissions import IsAuthenticated, AllowAny
from authentication.permissions import CustomDjangoModelPermission


class DefaultPermissionsMixin(object):
      permission_classes = [CustomDjangoModelPermission]

