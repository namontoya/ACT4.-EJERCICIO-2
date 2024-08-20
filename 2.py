#Ejercicio 4.2 Paquetes y métodos de acceso

class Inmueble:
    def __init__(self, id_inmobiliario, area, direccion):
        self.id_inmobiliario = id_inmobiliario
        self.area = area
        self.direccion = direccion

    def calcular_precio_venta(self):
        return self.area * self.precio_m2

    def mostrar_informacion(self):
        print(f"Identificador inmobiliario: {self.id_inmobiliario}")
        print(f"Área: {self.area} m2")
        print(f"Dirección: {self.direccion}")
        print(f"Precio de venta: ${self.calcular_precio_venta():,.0f}")


class Vivienda(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños):
        super().__init__(id_inmobiliario, area, direccion)
        self.num_habitaciones = num_habitaciones
        self.num_baños = num_baños

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de habitaciones: {self.num_habitaciones}")
        print(f"Número de baños: {self.num_baños}")


class CasaRural(Vivienda):
    precio_m2 = 1500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos, distancia_cabecera, altitud):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños)
        self.num_pisos = num_pisos
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud


class CasaUrbana(Vivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños)
        self.num_pisos = num_pisos


class CasaConjuntoCerrado(CasaUrbana):
    precio_m2 = 2500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos, valor_administracion, areas_comunes):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños, num_pisos)
        self.valor_administracion = valor_administracion
        self.areas_comunes = areas_comunes

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Valor de la administración: ${self.valor_administracion:,.0f}")
        print(f"Áreas comunes: {'Sí' if self.areas_comunes else 'No'}")


class CasaIndependiente(CasaUrbana):
    precio_m2 = 3000000


class Apartamento(Vivienda):
    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, valor_administracion):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños)
        self.valor_administracion = valor_administracion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Valor de la administración: ${self.valor_administracion:,.0f}")


class Apartaestudio(Apartamento):
    precio_m2 = 1500000

    def __init__(self, id_inmobiliario, area, direccion, num_habitaciones, num_baños, valor_administracion):
        super().__init__(id_inmobiliario, area, direccion, num_habitaciones, num_baños, valor_administracion)


class ApartamentoFamiliar(Apartamento):
    precio_m2 = 2000000


class Local(Inmueble):
    def __init__(self, id_inmobiliario, area, direccion, localizacion):
        super().__init__(id_inmobiliario, area, direccion)
        self.localizacion = localizacion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Localización: {'Interno' if self.localizacion == 'interno' else 'Da a la calle'}")


class LocalComercial(Local):
    precio_m2 = 3000000

    def __init__(self, id_inmobiliario, area, direccion, localizacion, centro_comercial):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.centro_comercial = centro_comercial

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Centro comercial: {self.centro_comercial}")


class Oficina(Local):
    precio_m2 = 3500000

    def __init__(self, id_inmobiliario, area, direccion, localizacion, es_gobierno):
        super().__init__(id_inmobiliario, area, direccion, localizacion)
        self.es_gobierno = es_gobierno

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Es gobierno: {'Sí' if self.es_gobierno else 'No'}")


#Prueba
def main(): 
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    apto1.mostrar_informacion()

    print("\n")

    aptestudio = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1, 0)
    aptestudio.mostrar_informacion()


if __name__ == "__main__":
    main()


