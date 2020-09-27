# Rest Framework
from rest_framework.permissions import IsAuthenticated, AllowAny


class DefaultPermissionsMixin(object):
      permission_classes = [AllowAny]