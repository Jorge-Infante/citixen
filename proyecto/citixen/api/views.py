from django.shortcuts import render

# Create your views here.
from producto.models import Producto, CompraProducto, Categoria
from .serializers import ProductoSerializer, CompraProductoSerializer, CategoriaSerializer
from rest_framework import viewsets, views

from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    content = {
        queryset
    }


class MarcarProducto(views.APIView):
    queryset = CompraProducto.objects.all()
    serializer_class = CompraProductoSerializer

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        producto = get_object_or_404(Producto, id=self.request.data.get('id', 0))
        comprado = CompraProducto.objects.create(producto=producto, usuario=request.user)
        comprado.save()

        content = {
            'id': producto.id,
            'comprado': True
        }
        return Response(content)


class ListarProductosCompradosViewSet(viewsets.ModelViewSet):
    queryset = CompraProducto.objects.all()
    serializer_class = CompraProductoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        productos_comprados = CompraProducto.objects.filter(
            usuario=request.user)
        serializer = CompraProductoSerializer(
            productos_comprados, many=True)

        return Response(serializer.data)
