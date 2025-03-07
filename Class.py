class Vehiculo:
    def __init__(self, marca: str, modelo: str, combustible: str, tipo: str, nivel_combustible: float, capacidad_tanque: float, consumo_por_km: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.tipo = tipo
        self.nivel_combustible = nivel_combustible
        self.capacidad_tanque = capacidad_tanque
        self.consumo_por_km = consumo_por_km

    def encender(self) -> str:
        if self.nivel_combustible < 0.1 * self.capacidad_tanque:
            return f" Advertencia: El {self.tipo} {self.marca} {self.modelo} tiene poco combustible. Debe ir a la gasolinera."
        return f"El {self.tipo} {self.marca} {self.modelo} está encendido."

    def arrancar(self) -> str:
        return f"El {self.tipo} {self.marca} {self.modelo} ha arrancado y usa {self.combustible} como combustible."

    def marchar(self, distancia: float) -> str:
        combustible_requerido = distancia * self.consumo_por_km
        if self.nivel_combustible <= 0:
            return f" El {self.tipo} {self.marca} {self.modelo} no puede moverse. Se quedó sin combustible."
        
        self.nivel_combustible -= combustible_requerido

        if self.nivel_combustible <= 0:
            self.nivel_combustible = 0
            return f" El {self.tipo} {self.marca} {self.modelo} se ha detenido. No tiene combustible."

        mensaje = f"El {self.tipo} {self.marca} {self.modelo} ha recorrido {distancia} km. Combustible restante: {self.nivel_combustible:.2f} gal."

        if self.nivel_combustible < 0.1 * self.capacidad_tanque:
            mensaje += "  Advertencia: Bajo nivel de combustible. Debe ir a la gasolinera."

        return mensaje

    def __str__(self) -> str:
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}, Combustible: {self.combustible}, Nivel: {self.nivel_combustible:.2f} gal"


class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, combustible: str, nivel_combustible: float, capacidad_tanque: float) -> None:
        super().__init__(marca, modelo, combustible, "Moto", nivel_combustible, capacidad_tanque, 0.05)


class Carro(Vehiculo):
    def __init__(self, marca: str, modelo: str, combustible: str, nivel_combustible: float, capacidad_tanque: float) -> None:
        super().__init__(marca, modelo, combustible, "Carro", nivel_combustible, capacidad_tanque, 0.1)


mi_moto = Moto("Yamaha", "XT660", "Corriente", 1.0, 10)
mi_carro = Carro("Mazda", "6", "Corriente", 12, 50)

print(mi_moto)
print(mi_moto.encender())
print(mi_moto.marchar(10))
print(mi_moto.marchar(5))
print(mi_moto.marchar(10))

print(mi_carro)
print(mi_carro.encender())
print(mi_carro.marchar(50))
print(mi_carro.marchar(80))
print(mi_carro.marchar(30))
