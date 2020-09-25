# convierte json a diccionario
from rest_framework import serializers
from django.contrib.auth.models import User
from producto.models import Producto, CompraProducto,Categoria


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('first_name')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.validationerror("este usuario ya existe")
        else:
            return data


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # fields = ['id', 'precio', 'stock', 'nombre', 'categoria']
        fields = '__all__'


class CompraProductoSerializer(serializers.ModelSerializer):
    # Traer la lista de productos
    producto = ProductoSerializer()

    class Meta:
        model = CompraProducto
        fields = ['producto']
