from AppCpder.views import *
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name = "home"),
    path('formulario/', formulario, name = "formulario"),
    path('registrar_Consorcista/', FormularioConsorcistaView.index, name="registrarConsorcista"),
    path('guardar_Consorcista/', FormularioConsorcistaView.procesar_formulario, name="guardarConsorcista"),
    path('listar_Consorcistas/', FormularioConsorcistaView.listar_consorcistas, name="listarConsorcistas"),
    path('registrar_Administrador/', FormularioAdministradorView.index, name="registrarAdministrador"),
    path('guardar_Administrador/', FormularioAdministradorView.procesar_formulario, name="guardarAdministrador"),
    path('listar_Administradores/', FormularioAdministradorView.listar_Administradores, name="listarAdministradores"),
    path('registrar_Expensa/', FormularioExpensaView.index, name="registrarExpensa"),
    path('guardar_Expensa/', FormularioExpensaView.procesar_formulario, name="guardarExpensa"),
    path('listar_Expensas/', FormularioExpensaView.listar_Expensas, name="listarExpensas"),
]
