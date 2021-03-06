# Rest Framework
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.response import Response

# Models
from .models import CustomUser
from django.contrib.auth.models import (Group, Permission)

# Serializers
from .serializers import (
    CustomUserSerializer, GroupSerializer, PermissionSerializer, WhoamiSerializer)

# Mixins
from utils.mixins.views import (ModelViewSetMixin, DefaultFiltersMixin)
from utils.mixins.permissions import DefaultPermissionsMixin


class CustomUserViewSet(DefaultPermissionsMixin, DefaultFiltersMixin, ModelViewSetMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def list(self, request, *args, **kwargs):
        fields = ('id', 'username', 'first_name', 'last_name',
                  'is_active', 'is_staff', "groups_permissions", 'groups', )
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, fields=fields, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(DefaultPermissionsMixin, DefaultFiltersMixin, viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ListPermissionView(DefaultPermissionsMixin, DefaultFiltersMixin, ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class WhoamiView(DefaultPermissionsMixin, ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = WhoamiSerializer

    def get_queryset(self):
        # Filter by current user
        usuarioActual = self.request.user.id
        obtenerUsuarioActual = self.queryset.filter(pk=usuarioActual)
        return obtenerUsuarioActual
