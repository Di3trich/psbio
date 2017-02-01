from django.contrib.auth.models import User, Group, Permission
from core.models import Persona, Horario, Registro, Dispositivo
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer, PersonaSerializer, HorarioSerializer, \
    RegistroSerializer, DispositivoSerializer


class PaginationControl(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 1000


class UserViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    pagination_class = PaginationControl


class GroupViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = PaginationControl


class PermissionViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = PaginationControl


class PersonaViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    pagination_class = PaginationControl


class DispositivoViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    pagination_class = PaginationControl


class HorarioViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    pagination_class = PaginationControl


class RegistroViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    pagination_class = PaginationControl
