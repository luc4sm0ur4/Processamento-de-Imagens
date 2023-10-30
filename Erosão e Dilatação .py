#Aluno: Lucas Carvalho da Luz Moura
#Matricula: 2020111816

import cv2
import numpy as np

def erosion(image, kernel_size):
    # Definindo o kernel para erosão
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Aplicando a erosão na imagem
    eroded_image = cv2.erode(image, kernel, iterations=1)

    return eroded_image

def dilation(image, kernel_size):
    # Definindo o kernel para dilatação
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Aplicar a dilatação na imagem
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    return dilated_image

# Carregar a imagem
image = cv2.imread('/home/lucasmoura/Área de trabalho/Projetos/Códigos para gravação/PI1.jpg', 0)

# Aplicando a erosão e dilatação na imagem
eroded_image = erosion(image, kernel_size=3)
dilated_image = dilation(image, kernel_size=3)

# Exibir as imagens resultantes
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem com Erosao', eroded_image)
cv2.imshow('Imagem com Dilatacao', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()