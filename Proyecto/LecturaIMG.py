import cv2
import numpy as np
import matplotlib.pyplot as plt
# from IPython.display import Image

#Lectura de imagenes
#Lectura en gray
imgray = cv2.imread("paisaje.jpeg", 0) #Cuando el segundo atributo está en 0, la imagen se lee en gray 1 canal 1 matriz

#Lectura en color
imgRGB = cv2.imread("paisaje.jpeg", 1) #Cuando el segundo atributo está en 1, la imagen se lee en color 3 canales 3 matriz

#Lectura
img = cv2.imread("paisaje.jpeg") #Cuando no ponemos un segundo atributo, leemos 3 canales en 3 matrices

#Extraer atributos principales
tama = imgray.shape #Tamaño de la imagen
tipo = imgray.dtype #Tipo de dato de la imagen
print("Tamaño Gray | Tipo de Dato", tama,  tipo)

#Extraer atributos principales
tamaRGB = imgRGB.shape #Tamaño de la imagen
tipoRGB = imgRGB.dtype #Tipo de dato de la imagen
print("Tamaño RGB | Tipo de Dato", tamaRGB,  tipoRGB)

#Mostramos las imagenes
cv2.imshow("Gray", imgray)
cv2.imshow("RGB", imgRGB)
cv2.imshow("IMG", img)

#Correccion de color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Mostramos nuestra imagen
plt.imshow(img)
plt.show()

#Con el teclado pasamos la imganen
#cv2.waitKey(0)