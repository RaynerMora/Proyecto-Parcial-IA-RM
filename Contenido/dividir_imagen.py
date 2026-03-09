from PIL import Image
import os

def dividir_guardar_imagen(ruta_imagen, carpeta_destino, divisiones_por_columna):
    #cagar imagen
    with Image.open(ruta_imagen) as img:
        img.load()

        ancho, alto = img.size

    #Calcular numero divisiones por fila para mantener la forma cuadrada
    tamaño_cuadrado = ancho // divisiones_por_columna
    divisiones_por_fila = alto // tamaño_cuadrado

    #Carpeta destino en caso no exista
    os.makedirs(carpeta_destino, exist_ok=True)

    #Dividir y Guardar tiled
    contador = 0
    for i in range(divisiones_por_fila):
        for j in range(divisiones_por_columna):
            contador += 1
            #coordenadas cuadrado
            izquierda = j * tamaño_cuadrado
            superior = i * tamaño_cuadrado
            derecha = izquierda + tamaño_cuadrado
            inferior = superior + tamaño_cuadrado

            #Cortar y Guardar Cuadrado
            cuadrado = img.crop((izquierda, superior, derecha, inferior))
            nombre_archivo = f"tile ({contador}).png"
            cuadrado.save(os.path.join(carpeta_destino, nombre_archivo))

    img.close()

dividir_guardar_imagen("assets/imagenes/tiles/mapa_type.png", carpeta_destino= "assets/imagenes/tiles", divisiones_por_columna=10)   

