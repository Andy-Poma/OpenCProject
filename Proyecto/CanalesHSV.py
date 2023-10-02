import cv2
import matplotlib.pyplot as plt

#Imagen
#Vamos a crear nuestra matriz principal
img = cv2.imread("paisaje.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Corregimos
imghsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#Extraemos los canales
H, S, V = cv2.split(imghsv)

#Mostramos nuestros canales
fig = plt.figure()
#Canal Rojo
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(H, cmap='gray')
ax1.set_title("Canal H")

#Canal Verde
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(S, cmap='gray')
ax2.set_title("Canal S")

#Canal Azul
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(V, cmap='gray')
ax3.set_title("Canal V")

#Reconstruccion
imgre = cv2.merge((H, S, V))

#Imagen original
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(img)
ax4.set_title("Imagen Original")
plt.show()
