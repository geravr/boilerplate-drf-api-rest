# Rest Framework
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Models
from .models import CustomUser

# Serializers
from .serializers import (CustomUserSerializer, WhoamiSerializer)

# Mixins
from utils.mixins.views import ModelViewSetMixin
from utils.mixins.permissions import DefaultPermissionsMixin


class CustomUserViewSet(DefaultPermissionsMixin, ModelViewSetMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        fields = ('id', 'username', 'first_name', 'last_name',
        'is_active', 'is_staff', 'groups', 'created_at', )
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, fields=fields, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class WhoamiView(DefaultPermissionsMixin, ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = WhoamiSerializer

    def get_queryset(self):
        # Filter by current user
        usuarioActual = self.request.user.id
        obtenerUsuarioActual = self.queryset.filter(pk=usuarioActual)
        return obtenerUsuarioActual