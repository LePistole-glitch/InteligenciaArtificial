import cv2
import matplotlib.pyplot as plt

# cargar imagen y conver a escala de grises
imagen = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)
#imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

#calcula el histograma
hist = cv2.calcHist([imagen], [0], None, [256], [0, 256])
#graficar histogramas
plt.plot(hist, color='black')
plt.xlabel('Densisdas de pixeles')
plt.ylabel('Frecuencia')
plt.title('Histograma de la imagen')
plt.savefig('histograma.png')  # Guardar la figura como una imagen
plt.show()