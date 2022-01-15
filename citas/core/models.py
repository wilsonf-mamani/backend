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
        ('no_especifica', 'NO_ESPECIFICA')
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
        default='NO_ESPECIFICA'
    )
    

    personaFoto = models.ImageField(
        db_column='foto',
        upload_to='personas/',
        null=True,

    )

    class Meta:
        