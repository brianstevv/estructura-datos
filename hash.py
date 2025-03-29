from typing import Optional

class DirectorioTelefonico:
    def __init__(self):
        self.directorio = {}
    
    def agregar_contacto(self, nombre: str, telefono: str) -> str:
        self.directorio[nombre] = telefono
        return f"Contacto {nombre} agregado exitosamente."
    
    def obtener_telefono(self, nombre: str) -> Optional[str]:
        return self.directorio.get(nombre, "Contacto no encontrado.")
    
    def eliminar_contacto(self, nombre: str) -> str:
        if nombre in self.directorio:
            del self.directorio[nombre]
            return f"Contacto {nombre} eliminado exitosamente."
        return "Contacto no encontrado."
    
    def mostrar_directorio(self):
        return self.directorio


directorio = DirectorioTelefonico()
print(directorio.agregar_contacto("brian", "188-956-70"))
print(directorio.obtener_telefono("brian"))
print(directorio.eliminar_contacto("brian"))
print(directorio.mostrar_directorio())
