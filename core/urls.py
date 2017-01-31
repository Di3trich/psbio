from rest_framework import routers
from django.conf.urls import url, include
from core.views import UserViewSet, PermissionViewSet, GroupViewSet, PersonaViewSet, HorarioViewSet, DispositivoViewSet, \
    RegistroViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'group', GroupViewSet)
router.register(r'horario', HorarioViewSet)
router.register(r'dispositivo', DispositivoViewSet)
router.register(r'registro', RegistroViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
