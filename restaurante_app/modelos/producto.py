class Producto:

    def __init__(
        self,
        nombre: str,
        precio: float,
        cantidad_disponible: int,
        disponible: bool
    ):

        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.disponible = disponible

    def mostrar_informacion(self):

        return f"{self.nombre} - ${self.precio}"

    def __str__(self):

        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio} | "
            f"Cantidad: {self.cantidad_disponible} | "
            f"Disponible: {self.disponible}"
        )