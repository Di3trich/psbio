from django.db import models
from datetime import datetime

TIPOS = [
    (1, 'Numero'),
    (2, 'Cadena'),
    (3, 'JSON'),
    (4, 'Booleano'),
    (5, 'Hora'),
    (6, 'Fecha'),
    (7, 'Fecha Hora')
]


class Configuracion(models.Model):
    nombre = models.CharField(max_length=128)
    valor = models.CharField(max_length=128)
    tipo = models.IntegerField(choices=TIPOS)

    def __str__(self):
        return "%s [%s]" % (self.nombre, self.valor)


class Dispositivo(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128, blank=True, null=True)
    actualizacion = models.DateTimeField(auto_now=True)

    @property
    def activo(self):
        diferencia = datetime.now() - self.actualizacion
        return diferencia.seconds < 60 * 15

    def __str__(self):
        return "%s" % self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Dispositivo, self).save(*args, **kwargs)


class Horario(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return "%s" % self.nombre

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super(Horario, self).save(*args, **kwargs)


class Persona(models.Model):
    codigo = models.IntegerField(unique=True)
    paterno = models.CharField(max_length=64)
    materno = models.CharField(max_length=64)
    nombres = models.CharField(max_length=128)
    email = models.EmailField(null=True, blank=True)
    dispositivo = models.ForeignKey(Dispositivo, related_name='personas')
    horario = models.ForeignKey(Horario, related_name='personas')

    def get_estado(self, fecha):
        justificacion = self.justificaciones.filter(fecha=fecha).first()
        feriado = Feriado.objects.filter(fecha=fecha).first()
        horario = self.horario.segmentos_horarios.all()
        marcas = self.registros.filter(marca=fecha)
        if justificacion != None and feriado != None:
            return "Justificacion, Feriado",
        if justificacion != None:
            return "Justificado", "%s" % justificacion
        if feriado != None:
            return "Feriado", "%s" % feriado
            # for segmento in horario:
            #   segmento.inicio >= fecha
        return "Falta", None

    def __str__(self):
        return "[%d] %s %s, %s" % (self.codigo, self.paterno, self.materno, self.nombres)

    @property
    def nombre_completo(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        self.paterno = self.paterno.upper()
        self.materno = self.materno.upper()
        self.nombres = self.nombres.upper()
        super(Persona, self).save(*args, **kwargs)


class Justificacion(models.Model):
    persona = models.ForeignKey(Persona, related_name='justificaciones')
    fecha = models.DateField()
    aval = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.persona, self.fecha)


class SegmentoHorario(models.Model):
    nombre = models.CharField(max_length=128)
    inicio = models.TimeField()
    final = models.TimeField()
    horario = models.ForeignKey(Horario, related_name='segmentos_horarios')

    def __str__(self):
        return "%s [%s - %s]" % (self.nombre, self.inicio, self.final)

    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        if self.inicio > self.final:
            self.inicio, self.final = self.final, self.inicio
        super(SegmentoHorario, self).save(*args, **kwargs)


class Registro(models.Model):
    marca = models.DateTimeField()
    persona = models.ForeignKey(Persona, related_name='registros')

    def __str__(self):
        return "%s (%s)" % (self.persona, self.marca)


class Reporte(models.Model):
    persona = models.ForeignKey(Persona, related_name='reportes')
    fecha = models.DateField()
    estado = models.CharField(max_length=128)
    justificacion = models.ForeignKey(Justificacion, null=True)

    @property
    def estado_calculado(self):
        estado, justificacion = self.persona.get_estado(self.marca)
        return estado

    def __str__(self):
        return "%s (%s) = %s" % (self.persona, self.fecha, self.estado)

    def save(self, *args, **kwargs):
        self.estado, self.justificacion = self.persona.get_estado(self.fecha)
        super(Reporte, self).save(*args, **kwargs)


class Feriado(models.Model):
    fecha = models.DateField()
    motivo = models.CharField(max_length=256)
    recurrente = models.BooleanField(default=False)

    def __str__(self):
        return "[%s] %s" % (self.fecha, self.motivo)
