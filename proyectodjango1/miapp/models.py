from django.db import models

# Create your models here.


class Libro(models.Model):
    nombre = models.CharField(max_length=45)
    decripcion = models.TextField()
    codigo = models.CharField(max_length=45)

    def __str__(self):
        return (self.nombre, self.decripcion, self.codigo)


class Ejemplar(models.Model):
    numeroEjemplar = models.CharField(max_length=45)
    fechaDeCompra = models.DateTimeField()
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return (self.numeroEjemplar, self.fechaDeCompra, self.libro)


class Prestamo(models.Model):
    fechaPrestamo = models.DateTimeField()
    nombreCliente = models.CharField(max_length=45)
    telefonoCliente = models.CharField(max_length=15)
    estado = models.BooleanField

    def __str__(self):
        return (self.fechaPrestamo, self.nombreCliente, self.telefonoCliente, self.estado)


class DetallePrestamo(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    ejemplar = models.ForeignKey(Ejemplar, on_delete=models.CASCADE)

    def __str__(self):
        return (self.prestamo, self.ejemplar)




