import cv2
import numpy as np
import matplotlib.pyplot as plt
#from IPython.display import Image

#Imagen
#Vamos a crear nuestra matriz principal
img = 100 * np.ones((10, 10, 3), np.uint8)

#Extraemos los canales
R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]

#Modificamos el canal Rojo
#R[:, :] = 0

#Modificamos el canal Verde
R[:, :] = 255
G[:, :] = 255
B[:, :] = 0

img[:,:,0] = R
img[:,:,1] = G
img[:,:,2] = B

print(img)

plt.imshow(img)
plt.show()

#cv2.waitKey(0)