#Para la división de equipamiento sustentable de EcoTech Solutions, 
# se requiere un módulo de software que gestione los productos del catálogo, 
# impida inconsistencias en el inventario mediante validaciones de negocio y 
# garantice la persistencia del stock en disco.

#Punto A: Dominio del Catálogo y Reglas de Inventario: 
# Construye la jerarquía orientada a objetos para los productos ecológicos. 
# Diseña una clase de excepción personalizada StockInvalidoError y 
# aplícala dentro de la clase base DispositivoEcológico para impedir que el stock 
# tome valores negativos mediante encapsulamiento explícito. 
# Desarrolla la clase especializada PanelSolar, incorporando sus atributos 
# específicos mediante herencia y aplicando polimorfismo para personalizar la 
# emisión de su ficha técnica comercial.

#Punto B: Persistencia y Gestión del Catálogo: Implementa la clase GestorInventario 
#con el método guardar_catalogo_json(lista_dispositivos, ruta_archivo) capaz de 
#serializar y almacenar en catalogo_ecotech.json las instancias creadas en el Punto A. 
#Incluye un bloque de prueba donde se verifique la captura controlada de 
#StockInvalidoError ante un intento de asignación de stock erróneo, finalizando con 
#la exportación exitosa de los productos válidos al archivo JSON.
import json
ruta_archivo = "Ejercicio2/catalogo_ecotech.json"

class StockInvalidoError(Exception):
    pass

class DispositivoEcologico:
    def __init__(self, nombre: str, stock: int, precio: float = 0.0):
        self.__nombre = nombre
        self.__stock = 0
        self.set_stock(stock)  
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_stock(self):
        return self.__stock

    def set_stock(self, valor):
        if valor < 0:
            raise StockInvalidoError("El stock no puede ser negativo.")
        self.__stock = valor

    def set_nombre(self, valor):
        self.__nombre = valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, valor):
        self.__precio = valor

    def ficha_tecnica(self):
        return f"Dispositivo: {self.__nombre}, Stock: {self.__stock}"


class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre: str, stock: int, precio: float, potencia: float):
        super().__init__(nombre, stock, precio)
        self.__potencia = potencia

    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, valor):
        self.__potencia = valor

    def ficha_tecnica(self):
        return f"Panel Solar: {self._DispositivoEcologico__nombre}, Stock: {self._DispositivoEcologico__stock}, Potencia: {self.__potencia}W"

class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos: list, ruta_archivo):
        with open(ruta_archivo, "w") as archivo:
            json.dump([dispositivo.__dict__ for dispositivo in lista_dispositivos], archivo, indent=4)

    def cargar_catalogo_json(self, ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            datos = json.load(archivo)
            lista_dispositivos = []
            for dispositivo in datos:
                if "potencia" in dispositivo:
                    panel = PanelSolar(dispositivo["_DispositivoEcologico__nombre"], dispositivo["_DispositivoEcologico__stock"], dispositivo["_DispositivoEcologico__precio"], dispositivo["_PanelSolar__potencia"])
                    lista_dispositivos.append(panel)
                else:
                    disp = DispositivoEcologico(dispositivo["_DispositivoEcologico__nombre"], dispositivo["_DispositivoEcologico__stock"], dispositivo["_DispositivoEcologico__precio"] )
                    lista_dispositivos.append(disp)
            return lista_dispositivos


#Bloque de prueba

heladera = DispositivoEcologico("Heladera Ecologica", 10, 500.0)
panel = PanelSolar("Panel Solar 300W", 5, 300.0, 300.0)

print(heladera.ficha_tecnica())
print(panel.ficha_tecnica())

try:
    frigorifico = DispositivoEcologico("Frigorífico Eficiente", -3, 400.0)
except StockInvalidoError as e:
    print("Error capturado:", e)

try:
    heladera.set_stock(-5)
except StockInvalidoError as e:
    print("Error capturado:", e)

lista_dispositivos = [heladera, panel]
gestor = GestorInventario()
gestor.guardar_catalogo_json(lista_dispositivos,ruta_archivo)

lista_carga = gestor.cargar_catalogo_json(ruta_archivo)
for dispositivo in lista_carga:
    print(dispositivo.ficha_tecnica())