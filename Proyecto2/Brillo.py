import cv2
import numpy as np
import matplotlib.pyplot as plt

#Leemos nuestra imagen
img = cv2.imread("paisaje.jpeg")
imgmat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Convertimos a EDG
