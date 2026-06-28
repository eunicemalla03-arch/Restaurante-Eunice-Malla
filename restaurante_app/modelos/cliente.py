class Cliente:

    def __init__(
        self,
        nombre: str,
        edad: int,
        correo: str,
        cliente_frecuente: bool
    ):

        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.cliente_frecuente = cliente_frecuente

    def __str__(self):

        return (
            f"Cliente: {self.nombre} | "
            f"Edad: {self.edad} | "
            f"Correo: {self.correo} | "
            f"Cliente frecuente: {self.cliente_frecuente}"
        )