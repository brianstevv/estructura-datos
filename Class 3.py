class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        return f"{self.nombre} está trabajando en el departamento de {self.departamento}."

    def obtener_info(self):
        return f"{self.nombre} tiene un salario de {self.salario} COP y trabaja como {self.__class__.__name__}."

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        return f"{self.nombre} está supervisando a su equipo de {len(self.equipo)} empleados."

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguaje_de_programacion):
        super().__init__(nombre, salario, departamento)
        self.lenguaje_de_programacion = lenguaje_de_programacion

    def trabajar(self):
        return f"{self.nombre} está escribiendo código en {self.lenguaje_de_programacion}."

Stiven = Desarrollador("Stiven", 4800000, "Desarrollador", "Python")
Deisy = Desarrollador("Deisy", 4700000, "Desarrollador", "Java")
gerente = Gerente("Brian", 70000000, "Gestión", [Stiven, Deisy])

print(gerente.trabajar())
print(gerente.obtener_info())
print(Stiven.trabajar())
print(Stiven.obtener_info())
print(Deisy.trabajar())
print(Deisy.obtener_info())


class FiguraGeometrica:
    def calcular_area(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

triangulo = Triangulo(10, 5)
cuadrado = Cuadrado(4)

print(f"Área del triángulo: {triangulo.calcular_area()}")
print(f"Área del cuadrado: {cuadrado.calcular_area()}")

class Electrodomestico:
    def __init__(self, marca, modelo, consumo_energetico):
        self.marca = marca
        self.modelo = modelo
        self.consumo_energetico = consumo_energetico

    def encender(self):
        return f"El {self.marca} {self.modelo} está encendido."

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, capacidad):
        super().__init__(marca, modelo, consumo_energetico)
        self.capacidad = capacidad

    def encender(self):
        return f"La lavadora {self.marca} {self.modelo} inicia el ciclo de lavado."

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, tiene_congelador):
        super().__init__(marca, modelo, consumo_energetico)
        self.tiene_congelador = tiene_congelador

    def encender(self):
        return f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura."

lavadora = Lavadora("Samsung", "EcoBubble", "1500W", 15)
refrigerador = Refrigerador("Samsung", "TwinCooling", "2000W", True)

print(lavadora.encender())
print(refrigerador.encender())


class Usuario:
    def __init__(self, nombre_de_usuario, contraseña):
        self.nombre_de_usuario = nombre_de_usuario
        self.contraseña = contraseña

    def iniciar_sesion(self, usuario, contraseña):
        if self.nombre_de_usuario == usuario and self.contraseña == contraseña:
            return f"{self.nombre_de_usuario} ha iniciado sesión correctamente."
        return "Inicio de sesión fallido."

class Administrador(Usuario):
    def gestionar_usuarios(self):
        return f"El administrador {self.nombre_de_usuario} está gestionando usuarios."

class Cliente(Usuario):
    def realizar_compra(self):
        return f"El cliente {self.nombre_de_usuario} ha realizado una compra."

admin = Administrador("Brian", "admin123")
cliente1 = Cliente("Stiven", "cliente456")
cliente2 = Cliente("Deisy", "cliente789")

print(admin.iniciar_sesion("Brian", "admin123"))
print(admin.gestionar_usuarios())
print(cliente1.iniciar_sesion("Stiven", "cliente456"))
print(cliente1.realizar_compra())
print(cliente2.iniciar_sesion("Deisy", "cliente789"))
print(cliente2.realizar_compra())
