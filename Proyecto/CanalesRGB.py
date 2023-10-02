import cv2
import numpy as np
import matplotlib.pyplot as plt
# from IPython.display import Image

#Imagen
#Vamos a crear nuestra matriz principal
img = cv2.imread("paisaje.jpeg")
# Corregimos
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Extraemos los canales
#R = img[:,:,0]
#G = img[:,:,1]
#B = img[:,:,2]

print(img)

#COmando
R, G, B = cv2.split(img)

fig = plt.figure()
#Canal rojo
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(R, cmap='gray')
ax1.set_title("Canal Rojo")

#Canal verde
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(G, cmap='Greens')
ax2.set_title("Canal Verde")

#Canal azul
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(B, cmap='Blues')
ax3.set_title("Canal Azul")

#Reconstruccion
imgre = cv2.merge((R, G, B))

#Imagen original
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("Imagen Original")

plt.show()

#Con el teclado pasamos la imagen
#cv2.waitKey(0)