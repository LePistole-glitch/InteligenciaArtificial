#Imprimir valores de pixeles de una imagen
from PIL import Image

#abrir imagen
imagen = Image.open('img.jpg')

#tamaño deseado (ancho, alto)
nueva_imagen = (100, 100)
#redimencionar la imagen
imagen_redimensionada = imagen.resize(nueva_imagen)
#guardar la imagen
imagen_redimensionada.save('img2.jpg')
imagen_redimensionada.show()