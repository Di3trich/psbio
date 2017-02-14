from django.contrib.auth.models import User, Group, Permission
from core.models import Dispositivo, Persona, Horario, Registro, SegmentoHorario, Reporte
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'groups', 'user_permissions', 'is_superuser')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'id', 'name', 'permissions')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('url', 'id', 'name')


class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    persona = serializers.PrimaryKeyRelatedField(queryset=Persona.objects.all())
    persona_name = serializers.StringRelatedField(source='persona', read_only=True)

    class Meta:
        model = Registro
        fields = ('url', 'id', 'marca', 'persona', 'persona_name')


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    dispositivo = serializers.PrimaryKeyRelatedField(queryset=Dispositivo.objects.all())
    dispositivo_name = serializers.StringRelatedField(source='dispositivo', read_only=True)

    class Meta:
        model = Persona
        fields = ('url', 'id', 'codigo', 'paterno', 'materno', 'nombres', 'email', 'dispositivo', 'dispositivo_name',
                  'nombre_completo')


class DispositivoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('url', 'id', 'codigo', 'nombre', 'descripcion', 'actualizacion', 'activo')


class SegmentoHorarioSerializer(serializers.HyperlinkedModelSerializer):
    horario = serializers.PrimaryKeyRelatedField(queryset=Horario.objects.all())
    horario_name = serializers.StringRelatedField(source='horario', read_only=True)

    class Meta:
        model = SegmentoHorario
        fields = ('url', 'nombre', 'inicio', 'final', 'horario', 'horario_name')


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    segmentos_horarios = SegmentoHorarioSerializer(many=True, read_only=True)

    class Meta:
        model = Horario
        fields = ('url', 'id', 'nombre', 'descripcion', 'segmentos_horarios')


class ReporteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reporte
        fields = ('url', 'id', 'persona', 'fecha', 'estado', 'estado_calculado', 'justificacion')
