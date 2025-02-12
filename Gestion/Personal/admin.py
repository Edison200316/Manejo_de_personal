from django.contrib import admin
from django import forms
from .models import Empleado, Departamento, Cargo, Salario, Beneficio

class EmpleadoForm(forms.ModelForm):
    fecha_contratacion = forms.DateField(widget=admin.widgets.AdminDateWidget)  # Selector de fecha

    class Meta:
        model = Empleado
        fields = '__all__'  # Usa todos los campos

class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoForm  # Usa el formulario corregido
    list_display = ('id', 'nombre', 'apellido', 'email', 'telefono', 'genero', 'fecha_contratacion', 'departamento')
    search_fields = ('nombre', 'apellido', 'email', 'departamento__nombre')
    list_filter = ('genero', 'departamento')
    ordering = ('id',)
    list_per_page = 20

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('id',)
    list_per_page = 20

class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('id',)
    list_per_page = 20

class SalarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'empleado', 'cargo', 'monto', 'fecha_actualizacion')
    search_fields = ('empleado__nombre', 'empleado__apellido', 'cargo__nombre')
    list_filter = ('fecha_actualizacion',)
    ordering = ('id',)
    readonly_fields = ('fecha_actualizacion',)
    list_per_page = 20

class BeneficioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('id',)
    list_per_page = 20

# Registrar los modelos con las configuraciones mejoradas
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Salario, SalarioAdmin)
admin.site.register(Beneficio, BeneficioAdmin)

# Personalizar el encabezado y título del Admin
admin.site.site_header = "Panel de Administración - Personal"
admin.site.site_title = "Administración de Personal"
admin.site.index_title = "Gestión de Recursos Humanos"


