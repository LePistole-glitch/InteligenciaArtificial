#1.- Cargar Modulos
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

#cargar dos imagenes MONUMENTO - PAISAJE

#abrir imagen
imagen_mmt = Image.open('monumento.jpg')
imagen_psj = Image.open('paisaje.jpg')

#tamaño deseado (ancho, alto)
nueva_imagen = (100, 100)
#redimencionar la imagen
imagen_mmt = imagen_mmt.resize(nueva_imagen)
imagen_psj = imagen_psj.resize(nueva_imagen)

imagen_mmt.save('img3.jpg')
imagen_psj.save('img4.jpg')

#Abrir con OpenCV
img_mnt = cv2.imread('img3.jpg')
img_psj = cv2.imread('img4.jpg')

#asegurarnos que tengan el mismo tamanio
img_psj = cv2.resize(img_psj, (img_mnt.shape[1], img_mnt.shape[0]))

#operacion logica AND
result_and = cv2.bitwise_and(img_mnt, img_psj)
#operacion logica OR
result_or = cv2.bitwise_or(img_mnt, img_psj)
#operacion logica NOT
result_not = cv2.bitwise_not(img_mnt)
#Op logica XOR
result_xor = cv2.bitwise_xor(img_mnt, img_psj)


#mostrar las imagenes con openCV
cv2.imshow('Imagen 1', img_mnt)
#cv2.imshow('Imagen 2', imagen_psj)
cv2.imshow('Imagen 3 [AND]', result_and)
cv2.imshow('Imagen 4 [OR]', result_or)
cv2.imshow('Imagen 5 [NOT]', result_not)
cv2.imshow('Imagen 6 [XOR]', result_xor)


plt.subplot(231), plt.imshow(cv2.cvtColor(img_mnt, cv2.COLOR_BGR2RGB)), plt.title("1")
plt.subplot(232), plt.imshow(cv2.cvtColor(img_psj, cv2.COLOR_BGR2RGB)), plt.title("2")
plt.subplot(233), plt.imshow(result_and), plt.title("AND")
plt.subplot(234), plt.imshow(result_or), plt.title("OR")
plt.subplot(235), plt.imshow(result_not), plt.title("NOT")
plt.subplot(236), plt.imshow(result_xor), plt.title("XOR")
plt.savefig('resultado.png')
plt.show()