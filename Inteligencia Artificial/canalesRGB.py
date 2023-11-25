#
import cv2

imagen = cv2.imread('img.jpg')
#dividir la imagen en canales R, G, B
canal_b, canal_g, canal_r = cv2.split(imagen)

#mostrar cada canal por separado

cv2.imshow('Canal Rojo', canal_r)
cv2.imshow('Canal Verde', canal_g)
cv2.imshow('Canal Azul', canal_b)

cv2.waitKey(0)
cv2.destroyAllWindows()