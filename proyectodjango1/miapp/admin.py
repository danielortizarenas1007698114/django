from django.contrib import admin

# Register your models here.

from .models import Libro, Ejemplar, Prestamo, DetallePrestamo

admin.site.register(Libro)
admin.site.register(Ejemplar)
admin.site.register(Prestamo)
admin.site.register(DetallePrestamo)