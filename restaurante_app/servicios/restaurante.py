from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:

    def __init__(self, nombre: str):

        self.nombre = nombre

        # Primero lista de clientes
        self.clientes: list[Cliente] = []

        # Después lista de productos
        self.productos: list[Producto] = []


    def agregar_cliente(
        self,
        cliente: Cliente
    ):

        self.clientes.append(cliente)


    def agregar_producto(
        self,
        producto: Producto
    ):

        self.productos.append(producto)


    def mostrar_clientes(self):

        print("\nCLIENTES REGISTRADOS")

        for cliente in self.clientes:
            print(cliente)


    def mostrar_productos(self):

        print("\nPRODUCTOS REGISTRADOS")

        for producto in self.productos:
            print(producto)