class Persona:
    def __init__(self, nombre="Brian", edad=22, genero="Masculino"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

persona = Persona()
persona.presentarse()


class CuentaBancaria:
    def __init__(self, titular, saldo=1000000, numero_de_cuenta="323486728"):
        self.titular = titular
        self.saldo = saldo
        self.numero_de_cuenta = numero_de_cuenta

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.saldo} COP")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo = cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo} COP")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo} COP")

persona = Persona()
persona.presentarse()

cuenta = CuentaBancaria(titular=persona, numero_de_cuenta="323486728")
cuenta.consultar_saldo()
cuenta.depositar(500000)
cuenta.retirar(2000000)
cuenta.retirar(300000)
cuenta.consultar_saldo()


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

rectangulo = Rectangulo(base=10, altura=5)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")



class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.radio

circulo = Circulo(radio=7)
print(f"Área del círculo: {circulo.calcular_area():.2f}")
print(f"Circunferencia del círculo: {circulo.calcular_circunferencia():.2f}")


class Libro:
    def __init__(self, titulo, autor, genero, anio):
        self.titulo, self.autor, self.genero, self.anio = titulo, autor, genero, anio

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nGénero: {self.genero}\nAño de Publicación: {self.anio}")

libro_simpson = Libro("Los Simpson y la Filosofía", "William Irwin", "Ensayo", 2001)
libro_simpson.mostrar_detalles()


class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo, self.artista, self.album, self.duracion = titulo, artista, album, duracion

    def reproducir(self):
        print(f"Reproduciendo: {self.titulo} - {self.artista}")

cancion = Cancion("Baile Inolvidable", "Bad Bunny", "Nadie Sabe Lo Que Va a Pasar Mañana", "3:21")
cancion.reproducir()

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_cantidad_disponible(self):
        return self.cantidad_disponible

    def set_cantidad_disponible(self, cantidad):
        self.cantidad_disponible = cantidad

    def calcular_total(self, cantidad):
        if cantidad > self.cantidad_disponible:
            return "Stock insuficiente"
        return cantidad * self.precio

producto = Producto("Laptop", 2500000, 5)
print(f"Total a pagar por 3 unidades LAPTOP SAMSUNG: {producto.calcular_total(3)} COP")


class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0

    def determinar_estado(self):
        return "Aprobado" if self.calcular_promedio() >= 3.0 else "Reprobado"

estudiante = Estudiante("Brian", 22, "3er semestre")
estudiante.agregar_calificacion(4.0)
estudiante.agregar_calificacion(3.5)
estudiante.agregar_calificacion(2.8)
print(f"Promedio: {estudiante.calcular_promedio():.2f}")
print(f"Estado: {estudiante.determinar_estado()}")