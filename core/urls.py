from rest_framework import routers
from django.conf.urls import url, include
from core.views import UserViewSet, PermissionViewSet, GroupViewSet, PersonaViewSet, HorarioViewSet, DispositivoViewSet, \
    RegistroViewSet, SegmentoHorarioViewSet, ReporteViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'group', GroupViewSet)
router.register(r'horario', HorarioViewSet)
router.register(r'dispositivo', DispositivoViewSet)
router.register(r'registro', RegistroViewSet)
router.register(r'user', UserViewSet)
router.register(r'segmento_horario', SegmentoHorarioViewSet)
router.register(r'reporte', ReporteViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
