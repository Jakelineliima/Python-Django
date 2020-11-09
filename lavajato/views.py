from rest_framework import viewsets
from lavajato.models import Veiculo, Cliente, Revisao
from lavajato.serializer import VeiculoSerializer, ClienteSerializer, RevisaoSerializer

from django.http import JsonResponse


class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VeiculosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class RevisaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Revisao.objects.all()
    serializer_class = RevisaoSerializer
