from django.contrib import admin
from .models import Alojamiento, Alojamiento_Completo, Alojamiento_sin_finalizar, Interes, CityTour, Destino, Favorito, Moneda,\
    Estado_Servicio, Evaluacion, Excursion, Foto_Habitacion, Foto_Servicio, Habitacion, Habitacion_Alojamiento_Por_Habitacion,\
    Marca, Municipio, Pack, Pais, Provincia, Recorrido, Regla_Precio, Reserva, Idioma, Indisponibilidad, Servicio,\
    Taxi, Tipo_Alojamiento, Tour, Comision, Reserva_Habitacion, Tipo_Cambio, Foto_Destino, Regla_Cancelacion, Cancelacion_Reserva

# Register your models here.
admin.site.register(Alojamiento)
admin.site.register(Alojamiento_Completo)
admin.site.register(Alojamiento_sin_finalizar)
admin.site.register(Cancelacion_Reserva)
admin.site.register(CityTour)
admin.site.register(Comision)
admin.site.register(Destino)
admin.site.register(Estado_Servicio)
admin.site.register(Evaluacion)
admin.site.register(Excursion)
admin.site.register(Favorito)
admin.site.register(Foto_Destino)
admin.site.register(Foto_Habitacion)
admin.site.register(Foto_Servicio)
admin.site.register(Habitacion)
admin.site.register(Habitacion_Alojamiento_Por_Habitacion)
admin.site.register(Idioma)
admin.site.register(Indisponibilidad)
admin.site.register(Interes)
admin.site.register(Marca)
admin.site.register(Moneda)
admin.site.register(Municipio)
admin.site.register(Pack)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Recorrido)
admin.site.register(Regla_Cancelacion)
admin.site.register(Regla_Precio)
admin.site.register(Reserva)
admin.site.register(Reserva_Habitacion)
admin.site.register(Servicio)
admin.site.register(Taxi)
admin.site.register(Tipo_Alojamiento)
admin.site.register(Tipo_Cambio)
admin.site.register(Tour)