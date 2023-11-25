#Librerias
import cv2
import matplotlib.pyplot as plt
import numpy as np

#cargar una imagen
imagen = cv2.imread('img2.jpg')

#convertir figura a escala de grises
img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
#filtro desenfoque (blur)
img_blur = cv2.GaussianBlur(img_gris, (5,5), 0)

#filtro de deteccion de bordes(filtro canny)
img_borde = cv2.Canny(img_gris, 50, 150)

#definir un kernel para el filtro de realce (sharpen)

kernel = np.array([[-1,-1,-1], 
                   [-1,9,-1],
                   [-1,-1,-1]])
#aplicar filtro
img_realzada = cv2.filter2D(img_gris, -1, kernel)


plt.figure(figsize=(10,5)) #cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
plt.subplot(231), plt.imshow(imagen), plt.title("Original")
plt.subplot(232), plt.imshow(img_gris), plt.title("Gris")
plt.subplot(233), plt.imshow(img_blur), plt.title("Desenfoque")
plt.subplot(234), plt.imshow(img_borde), plt.title("Bordes")
plt.subplot(235), plt.imshow(img_realzada), plt.title("Realce")
plt.savefig('filtros.png')  # Guardar la figura como una imagen
plt.show()


#Histogramas
#calcula el histograma
imagen = np.clip(imagen, 0, 255)
img_gris = np.clip(img_gris, 0, 255)
img_blur = np.clip(img_blur, 0, 255)
img_borde = np.clip(img_borde, 0, 255)
img_realzada = np.clip(img_realzada, 0, 255)

hist_1 = cv2.calcHist([imagen], [0], None, [256], [0, 256])
hist_2 = cv2.calcHist([img_gris], [0], None, [256], [0, 256])
hist_3 = cv2.calcHist([img_blur], [0], None, [256], [0, 256])
hist_4 = cv2.calcHist([img_borde], [0], None, [256], [0, 256])
hist_5 = cv2.calcHist([img_realzada], [0], None, [256], [0, 256])


#graficar histogramas
plt.figure(figsize = (10, 6))
plt.subplot(151), plt.plot(hist_1, color='black'), plt.title('Original')
plt.subplot(152), plt.plot(hist_2, color='blue'), plt.title('Gris')
plt.subplot(153), plt.plot(hist_3, color='orange'), plt.title('Blur')
plt.subplot(154), plt.plot(hist_4, color='green'), plt.title('Borde')
plt.subplot(155), plt.plot(hist_5, color='red'), plt.title('Realzada')
plt.savefig('histograma.png')  # Guardar la figura como una imagen
plt.show()