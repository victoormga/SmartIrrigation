from rest_framework.routers import DefaultRouter
from .views import ParcelaViewSet


router = DefaultRouter()
router.register(r'parcelas', ParcelaViewSet, basename='parcela')


urlpatterns = router.urls