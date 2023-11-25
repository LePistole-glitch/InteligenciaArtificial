import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread('img2.jpg')

#convertir la img a escala de grises
img_gris = cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
#APLICA LA BINARICACION
_, imagen_binaria = cv2.threshold(img_gris, 128, 255, cv2.THRESH_BINARY)

#mostar las imagenes 
plt.subplot(131), plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(132), plt.imshow(img_gris, cmap='gray'), plt.title('Grises')
plt.subplot(133), plt.imshow(imagen_binaria, cmap='gray'), plt.title('Binarisada')

plt.show()