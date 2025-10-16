from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ReservaViewSet

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('reservas', ReservaViewSet)

urlpatterns = router.urls
