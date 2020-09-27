from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.views import APIView

class DocsView(APIView):
    """
    API REST
    """
    def get(self, request, *args, **kwargs):
        apidocs = {
                    'Root auth': request.build_absolute_uri('auth/'),
                   }
        return Response(apidocs)

urlpatterns = [
    path('api/v1/', DocsView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
]