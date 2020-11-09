
from django.contrib import admin
from django.urls import path, include
from lavajato.views import ClientesViewSet, VeiculosViewSet, RevisaoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)
router.register('veiculos', VeiculosViewSet)
router.register('revisaos', RevisaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
