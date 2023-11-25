#imprimir el valor de la matriz de pixeles
from PIL import Image
import time
#abrir la imagen
imagen = Image.open('img2.jpg')

#obtener las dienciones de la imagen
ancho, alto = imagen.size
print(imagen.size)

#imprimir los valores de los pixeles
for y in range(alto):
    for x in range(ancho):
        #obtener el valor del pixel en RGB
        pixel = imagen.getpixel((x,y))
        print(f'coordenadas: ({x}, {y}), valor del pixel: {pixel}')
        time.sleep(5)