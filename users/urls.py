from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, PolicyViewSet, RoleViewSet, Login

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'policy', PolicyViewSet)
router.register(r'role', RoleViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login', Login.as_view(), name='Login'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
]