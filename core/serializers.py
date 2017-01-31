from django.contrib.auth.models import User, Group, Permission
from core.models import Dispositivo, Persona, Horario, Registro
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'user_permissions', 'is_superuser')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'permissions')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'name')


class DispositivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('url', 'codigo', 'nombre', 'descripcion')


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('url', 'codigo', 'paterno', 'materno', 'nombres', 'email', 'dispositivo')


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('url', 'nombres', 'descripcion', 'inicio', 'final')


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registro
        fields = ('url', 'marca', 'persona')
