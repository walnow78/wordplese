# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    # Como lo tengo tanto para el envio como lectura lo dejo readonly
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de user a partri de
        validated_data que contienen valores deserializados
        :param validated_data: Diccionario con datos de usuario
        :return: objeto User
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiz una instancia de user a partri de los datos
        del diccionario lvalidated_data que contiene valores
        deserializados
        :param instance: objeto User
        :param validated_data: diccionario con los nuevos valores para el user
        :return: User actualizado
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        # Paso la contraseña encriptada
        instance.set_password(validated_data.get('password'))
        # Guardo el usuario
        instance.save()

        return instance


    # Validaciones
    def validate_username(self, data):
        users = User.objects.filter(username=data)
        # Si estoy crando (no tengo una instancia)
        # Existe usuario registrado
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        # Si estoy actualizando (tengo instancia y es diferente al nuevo usuario que me están pasando)
        # Existe usuario registrado
        elif self.instance != data and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese username")
        else:
            return data
