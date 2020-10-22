# Django
from django.urls import path
from django.conf.urls import url, include

# Rest Framework
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.views import APIView

# Views
from .views import (CustomUserViewSet, GroupViewSet, ListPermissionView, WhoamiView)

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, 'users')
router.register(r'groups', GroupViewSet, 'groups')

class AuthView(APIView):
    """
    Authentication Endpoints
    """
    def get(self, request, *args, **kwargs):
        apidocs = {
                    'Users': request.build_absolute_uri('users/'),
                    'Groups': request.build_absolute_uri('groups/'),
                    'Permissions': request.build_absolute_uri('permissions/'),
                    'Whoami': request.build_absolute_uri('whoami/'),
                    'Token Obtain': request.build_absolute_uri('token/obtain/'),
                    'Token Refresh': request.build_absolute_uri('token/refresh/'),
                   }
        return Response(apidocs)

urlpatterns = [
    path('', AuthView.as_view()),
    url(r'^', include(router.urls)),
    path('permissions/', ListPermissionView.as_view()),
    path('whoami/', WhoamiView.as_view()),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]