import cv2
import numpy as np
import matplotlib.pyplot as plt
#from IPython.display import Image

#Imagen
#Vamos a crear nuestra matriz principal
img = cv2.imread("paisaje.jpeg")
# Corregimos
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img)

#Extraemos los canales
R, G, B = cv2.split(img)

#Mostramos nuestros canales
fig = plt.figure()
#Canal rojo
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(R, cmap='Reds')
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
imgre = cv2.merge((R+100, G, B)) #Aumentamos el canal rojo

#Imagen original
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(imgre)
ax4.set_title("Imagen Original")

imgre = cv2.cvtColor(imgre, cv2.COLOR_RGB2BGR)
cv2.imwrite("NuevaImagen.jpeg", imgre)

plt.show()