import cv2
import matplotlib.pyplot as plt
import numpy as np

#cargar la imagen
imagen = cv2.imread('img2.jpg')


#valor escalar a la imagen
img_suma = cv2.add(imagen, 3000)

img_resta = cv2.subtract(imagen, 99)

img_mult = cv2.multiply(imagen, 4.11)


#
img_suma = np.clip(img_suma, 0, 255)
img_resta = np.clip(img_resta, 0, 255)
img_mult = np.clip(img_mult, 0, 255)


#calcula el histograma
hist_1 = cv2.calcHist([imagen], [0], None, [256], [0, 256])
hist_2 = cv2.calcHist([img_resta], [0], None, [256], [0, 256])
hist_3 = cv2.calcHist([img_suma], [0], None, [256], [0, 256])
hist_4 = cv2.calcHist([img_mult], [0], None, [256], [0, 256])
#Mostrar imagenes ori y procesadas
plt.figure(figsize = (10, 3))
plt.subplot(141), plt.imshow(imagen), plt.title('Original')
plt.subplot(142), plt.imshow(img_suma), plt.title('')
plt.subplot(143), plt.imshow(img_resta), plt.title('')
plt.subplot(144), plt.imshow(img_mult), plt.title('')
plt.savefig('transformaciones.png')  # Guardar la figura como una imagen
plt.show()


#graficar histogramas
plt.figure(figsize = (10, 6))
plt.subplot(141), plt.plot(hist_1, color='black')
plt.subplot(142), plt.plot(hist_2, color='black')
plt.subplot(143), plt.plot(hist_3, color='black')
plt.subplot(144), plt.plot(hist_4, color='black')
plt.savefig('histograma.png')  # Guardar la figura como una imagen
plt.show()