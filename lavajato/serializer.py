from rest_framework import serializers
from lavajato.models import Veiculo, Cliente, Revisao


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        field = ['id', 'modelo', 'placa', 'cor', 'fabricacao']


class RevisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revisao
        field = ['id', 'placa', 'fabricacao', 'revisao']
