from django.contrib import admin
from lavajato.models import Cliente, Veiculo, Revisao


class Veiculos(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'placa', 'cor', 'fabricacao')
    list_display_links = 'placa'
    search_fields = ('placa',)


admin.site.register(Veiculo, Veiculos)


class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'cpf')
    search_fields = 'cpf'
    list_per_page = 20


admin.site.register(Cliente, Clientes)


class Revisaos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'Veiculo', 'revisao')
    list_display_links = ('id',)


admin.site.register(Revisao, Revisaos)
