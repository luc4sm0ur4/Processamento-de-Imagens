#Aluno : Lucas Carvalho da Luz Moura
#Matricula: 2020111816

import cv2
import numpy as np

def apply_mean_filter(image, kernel_size):
    # Copia a imagem original
    filtered_image = image.copy()
    height, width = image.shape[:2]

    # Calculando a metade do tamanho do kernel
    kernel_half = kernel_size // 2

    # Aplicando o filtro de média em todos os pixels, exceto nas bordas da imagem
    for y in range(kernel_half, height - kernel_half):
        for x in range(kernel_half, width - kernel_half):
            # Obtendo a vizinhança do pixel atual
            neighborhood = image[y - kernel_half:y + kernel_half + 1, x - kernel_half:x + kernel_half + 1]

            # Calculando a média dos valores dos pixels na vizinhança
            average = np.mean(neighborhood)

            # Atribuindo o valor médio ao pixel na imagem filtrada
            filtered_image[y, x] = average

    return filtered_image

# Carregando a imagem de entrada
image = cv2.imread('/home/lucasmoura/Área de trabalho/Projetos/Códigos para gravação/PI1.jpg', cv2.IMREAD_GRAYSCALE) 

# Define o tamanho do kernel para o filtro de média
kernel_size = 3

# Aplicando o filtro de média com tratamento de bordas
filtered_image = apply_mean_filter(image, kernel_size)

# Exibe a imagem de entrada e a imagem filtrada
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Filtrada', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()