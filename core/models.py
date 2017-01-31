from django.db import models


class Dispositivo(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128)

    def __str__(self):
        return "%s" % self.nombre


class Persona(models.Model):
    codigo = models.IntegerField(unique=True)
    paterno = models.CharField(max_length=64)
    materno = models.CharField(max_length=64)
    nombres = models.CharField(max_length=128)
    email = models.EmailField()
    dispositivo = models.ForeignKey(Dispositivo)

    def __str__(self):
        return "[%d] %s %s %s" % (self.codigo, self.paterno, self.materno, self.nombres)


class Horario(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128)
    inicio = models.TimeField()
    final = models.TimeField()

    def __str__(self):
        return "%s %s %s" % (self.descripcion, self.inicio, self.final)


class Registro(models.Model):
    marca = models.DateTimeField()
    persona = models.ForeignKey(Persona)

    def __str__(self):
        return "%s (%s)" % (self.persona, self.marca)
