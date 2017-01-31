from django.contrib.auth.models import User, Group, Permission
from core.models import Persona, Horario, Registro, Dispositivo
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer, PersonaSerializer, HorarioSerializer, \
    RegistroSerializer, DispositivoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class DispositivoViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer


class HorarioViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer


class RegistroViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
