import os

# Ruta de la carpeta con las imágenes
carpeta_imagenes = "C:\\Users\\tu\\Desktop\\dentirect\\fotos_bollos"

# Prefijo para los nuevos nombres
prefijo = "bollo_"
# Extensiones de archivo que deseas renombrar
extensiones = [".jpg", ".png", ".jpeg"]

# Renombrar las imágenes
def renombrar_imagenes(carpeta, prefijo, extensiones):
    # Listar todos los archivos en la carpeta
    archivos = os.listdir(carpeta)
    contador = 1

    for archivo in archivos:
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)

        # Verificar si el archivo tiene una extensión válida
        if extension.lower() in extensiones:
            # Crear el nuevo nombre
            nuevo_nombre = f"{prefijo}{contador}{extension}"

            # Rutas completa del archivo original y el nuevo nombre
            ruta_original = os.path.join(carpeta, archivo)
            ruta_nueva = os.path.join(carpeta, nuevo_nombre)

            # Renombrar el archivo
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrado: {archivo} -> {nuevo_nombre}")

            contador += 1

# Llamar a la función
renombrar_imagenes(carpeta_imagenes, prefijo, extensiones)