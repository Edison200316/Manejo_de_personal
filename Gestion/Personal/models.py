from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    GENEROS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENEROS)
    fecha_contratacion = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, related_name='empleados')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cargo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre

class Salario(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, related_name='salario')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='salarios')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.empleado.nombre} {self.empleado.apellido} - ${self.monto}"

class Beneficio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    empleados = models.ManyToManyField(Empleado, related_name='beneficios')

    def __str__(self):
        return self.nombre
