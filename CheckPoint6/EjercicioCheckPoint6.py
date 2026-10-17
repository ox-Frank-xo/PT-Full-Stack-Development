class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

mi_usuario = Usuario("carlos_dev", "MiPasswordSeguro123!")

print(f"Nombre de usuario: {mi_usuario.nombre_usuario}")
print(f"Contraseña: {mi_usuario.contraseña}")