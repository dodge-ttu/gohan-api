from django.urls import path, include
from rest_framework.routers import DefaultRouter

from devices import views

router = DefaultRouter()
router.register('device', views.DeviceViewSet)
router.register('devicetype', views.DevicetypeViewSet)
router.register('locations', views.LocationViewSet)
router.register('wxstatreadings', views.WxstatreadingViewSet)
router.register('soilprobereadings', views.SoilprobereadingViewSet)
router.register('raingaugereadings', views.RaingaugereadingViewSet)
router.register('tankmonitorreadings', views.TankmonitorreadingViewSet)

app_name = 'devices'

urlpatterns = [
    path('', include(router.urls))
]
