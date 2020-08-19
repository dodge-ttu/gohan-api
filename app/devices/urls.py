from django.urls import path, include
from rest_framework.routers import DefaultRouter

from devices import views


router = DefaultRouter()
router.register('devicetags', views.DevicetagViewSet)

app_name = 'devices'

urlpatterns = [
    path('', include(router.urls))
]
