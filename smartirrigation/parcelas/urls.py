from rest_framework.routers import DefaultRouter
from .views import ParcelaViewSet, SensorViewSet, LecturaViewSet


router = DefaultRouter()
router.register(r'parcelas', ParcelaViewSet, basename='parcela')
router.register(r'sensores', SensorViewSet, basename='sensor')
router.register(r'lecturas', LecturaViewSet, basename='lectura')


urlpatterns = router.urls