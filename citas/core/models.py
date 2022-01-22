from distutils.command.upload import upload
from django.db import models

# Create your models here.


class PersonaModel(models.Model):
    opcionesEstadoCivil = [
        ('soltero', 'SOLTERO'),
        ('casado', 'CASADO'),
        ('viudo', 'VIUDO'),
        ('divorciado', 'DIVORCIADO'),
        ('complicado', 'COMPLICADO'),                        
        ('no_especifica', 'NO_ESPECIFICA'),
    ]


    personaId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )
    personaNombre = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='nombre'
    )

    personaApellido = models.CharField(
        max_length=50,
        unique=False,
        null=False,
        db_column='apellido'
    )

    personaEmail = models.EmailField(
        max_length=50,
        unique=True,
        null=False,
        db_column='email'
    )

    personaFechaNacimiento = models.DateField(
        db_column='fech_nac'
    )

    personaEstadoCivil = models.CharField(
        choices=opcionesEstadoCivil,
        db_column='estado_civil',
        default='NO_ESPECIFICA',
        max_length=50
    )
    

    personaFoto = models.ImageField(
        db_column='foto',
        upload_to='personas/',
        null=True,

    )

    class Meta:
        db_table = 'personas'

class CitaModel(models.Model):
    opcionesEstado = [
        ('ACTIVA','ACTIVA'),
        ('CANCELADA','CANCELADA'),
        ('POSPUESTA','POSPUESTA'),
    ]


    citaId = models.AutoField(
        primary_key=True,
        unique=True,
        null=False,
        db_column='id'
    )
    citaDescripcion = models.TextField(
        null=False,
        db_column='descripcion'
    )

    citaFecha = models.DateTimeField(
        null=False,
        db_column='fecha'
    )

    citaLatitud = models.FloatField(
        null=False,
        db_column='latitud'
    )

    citaLongitud = models.FloatField(
        null=False,
        db_column='longitud'
    )

    
    personaEstadoCivil = models.CharField(
        choices=opcionesEstado,
        db_column='estado',
        null=False,
        max_length=50,
    )
    
    
    createdAt = models.DateTimeField(
        auto_now=True,
        db_column='create_at'
    )


    updateAt = models.DateTimeField(
        auto_now=True,
        db_column='updated_at'
    )


    citador = models.ForeignKey(
        to=PersonaModel,
        db_column='citador_id',
        on_delete=models.PROTECT,
        related_name='personaCitas'
    )

    citado = models.ForeignKey(
        to=PersonaModel,
        db_column='citado_id',
        on_delete=models.PROTECT,
        related_name='personaCitadas'
    )

    class Meta:
        db_table = 'citas'
        unique_together =[['citaFecha','citador'],['citaFecha','citado']]
        ordering = ['-citaFecha']

        