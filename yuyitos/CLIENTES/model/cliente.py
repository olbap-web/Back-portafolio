from django.db import models

#serializers
from rest_framework import serializers

from core.model.base import Base


class Cliente(Base):

    nombres = models.CharField(max_length=120,
                                blank=False,
                                null=False,
                                verbose_name="Nombres")
    paterno = models.CharField(max_length=80,
                                blank=False,
                                null=False,
                                verbose_name="Apellido Paterno")
    materno = models.CharField(max_length=80,
                                blank=False,
                                null=False,
                                verbose_name="Apellido Materno")
    telefono = models.IntegerField(max_length=9,
                                blank=False,
                                null=False,
                                verbose_name="Teléfono Móvil")
    autorizado = models.BooleanField(blank=False,
                                null=False,
                                verbose_name="Autorizado")
    direccion = models.CharField(max_length=255,
                                blank=False,
                                null=False,
                                verbose_name="Dirección")
    

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "cli_cliente"


    def __str__(self):
        nom_completo = str(self.nombres) + ' ' + str(self.paterno) + ' ' + str(self.materno)
        return nom_completo

    def validar(self):

        error=[]
        if not self.nombres:
            error.append("El nombre es obligatorio")

        if not self.direccion:
            error.append("La dirección es obligatoria")

        if len(str(self.cod_ensenianza))>4:
            error.append("El codigo '"+self.cod_ensenianza+"' es demasiado largo ("+str(len(self.cod_ensenianza))+" caracteres )")

        if len(str(self.desc_ensenianza))>100:
            error.append("la descripcion '"+self.desc_ensenianza+"' es demasiado largo ("+str(len(self.desc_ensenianza))+" caracteres )")

        return error

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'nombres',
            'paterno',
            'materno',
            'telefono',
            'autorizado',
            'direccion',
        )