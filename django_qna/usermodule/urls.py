from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
]
