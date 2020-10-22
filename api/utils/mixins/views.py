# Rest_framework
from rest_framework import filters, viewsets, status
from rest_framework.response import Response
from datetime import datetime

# Filters
from django_filters import rest_framework as filters_rest

class DefaultFiltersMixin(object):
    filter_backends = (filters_rest.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter,)
    paginate_by = 30
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class ModelViewSetMixin(viewsets.ModelViewSet):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = datetime.now()
        instance.save()
        response = {
            "result": "Eliminado correctamente"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)