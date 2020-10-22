from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from collections import OrderedDict

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('total_pages', self.page.paginator.num_pages),
            ('results', data)
        ]))