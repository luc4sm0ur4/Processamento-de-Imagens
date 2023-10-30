#Aluno: Lucas Carvalho da Luz Moura
#Matricula: 2020111816

import cv2
import numpy as np

def gradient_filter(image):
    # Aplicando as máscaras de Sobel
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculando a magnitude do gradiente
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalizando a magnitude do gradiente
    gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    return gradient_magnitude

# Carregando a imagem
image = cv2.imread('/home/lucasmoura/Área de trabalho/Projetos/Códigos para gravação/PI1.jpg', 0)  

# Aplicando o filtro de gradiente usando a máscara de Sobel
filtered_image = gradient_filter(image)

# Exibindo as imagens resultantes
cv2.imshow('Original', image)
cv2.imshow('Imagem com Filtro Gradiente com Mascara de Sobel', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()