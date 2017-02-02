from django.db import models


class Dispositivo(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return "%s" % self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Dispositivo, self).save(*args, **kwargs)

class Persona(models.Model):
    codigo = models.IntegerField(unique=True)
    paterno = models.CharField(max_length=64)
    materno = models.CharField(max_length=64)
    nombres = models.CharField(max_length=128)
    email = models.EmailField(null=True, blank=True)
    dispositivo = models.ForeignKey(Dispositivo, related_name='personas')

    def __str__(self):
        return "[%d] %s %s %s" % (self.codigo, self.paterno, self.materno, self.nombres)

    def save(self, *args, **kwargs):
        self.paterno = self.paterno.upper()
        self.materno = self.materno.upper()
        self.nombres = self.nombres.upper()
        super(Persona, self).save(*args, **kwargs)


class Horario(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128, blank=True, null=True)
    inicio = models.TimeField()
    final = models.TimeField()

    def __str__(self):
        return "%s %s %s" % (self.descripcion, self.inicio, self.final)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Horario, self).save(*args, **kwargs)


class Registro(models.Model):
    marca = models.DateTimeField()
    persona = models.ForeignKey(Persona)

    def __str__(self):
        return "%s (%s)" % (self.persona, self.marca)
