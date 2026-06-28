from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante


# Crear restaurante
restaurante = Restaurante(
    "Sabores del Valle"
)


# Crear clientes
cliente1 = Cliente(
    "María López",
    28,
    "maria@gmail.com",
    True
)

cliente2 = Cliente(
    "Carlos Pérez",
    35,
    "carlos@gmail.com",
    False
)


# Crear productos
producto1 = Producto(
    "Hamburguesa",
    6.50,
    20,
    True
)

producto2 = Producto(
    "Jugo Natural",
    2.75,
    15,
    True
)


# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)


# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)


# Mostrar información
print("\nSISTEMA DE GESTIÓN DE RESTAURANTE")
print("--------------------------------")

restaurante.mostrar_clientes()
restaurante.mostrar_productos()