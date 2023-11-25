#Importar libreras
import cv2
import numpy as np
import matplotlib.pyplot as plt

#cargar la imagen
imagen = cv2.imread('img2.jpg')

#Escala DE GRISES
img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#valor escalar a la imagen
img_suma = cv2.add(img_gris, 150)

img_resta = cv2.subtract(img_gris, 150)

img_mult = cv2.multiply(img_gris, 1.25)


#
img_suma = np.clip(img_suma, 0, 255)
img_resta = np.clip(img_resta, 0, 255)
img_mult = np.clip(img_mult, 0, 255)

#Mostrar imagenes ori y procesadas
plt.figure(figsize = (10, 3))
plt.subplot(141), plt.imshow(img_gris, cmap='gray'), plt.title('Original')
plt.subplot(142), plt.imshow(img_suma, cmap='gray'), plt.title('')
plt.subplot(143), plt.imshow(img_resta, cmap='gray'), plt.title('')
plt.subplot(144), plt.imshow(img_mult, cmap='gray'), plt.title('')

plt.show()