#Aluno: Lucas Carvalho da Luz Moura\
#Matricula: 2020111816

import cv2
import numpy as np

def laplacian_filter(image, mask_type):
    # Definindo as máscaras
    masks = {
        'Mascara 1': np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),
        'Mascara 2': np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]]),
        'Mascara 3': np.array([[2, -1, 2], [-1, -4, -1], [2, -1, 2]]),
        'Mascara 4': np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    }

    # Onde é selecionado a máscara com base no tipo fornecido
    mask = masks.get(mask_type)

    # Aplicação do filtro Laplaciano na imagem
    filtered_image = cv2.filter2D(image, -1, mask)

    return filtered_image

# Carregando a imagem
image = cv2.imread('/home/lucasmoura/Área de trabalho/Projetos/Códigos para gravação/PI1.jpg', 1)  

# Aplicação do filtro Laplaciano com diferentes máscaras
filtered_image1 = laplacian_filter(image, 'Mascara 1')
filtered_image2 = laplacian_filter(image, 'Mascara 2')
filtered_image3 = laplacian_filter(image, 'Mascara 3')
filtered_image4 = laplacian_filter(image, 'Mascara 4')

# Exibindo as imagens resultantes
cv2.imshow('Original', image)
cv2.imshow('Imagem Filtrada - Laplaciano(Mascara 1)', filtered_image1)
cv2.imshow('Imagem Filtrada - Laplaciano (Mascara 2)', filtered_image2)
cv2.imshow('Imagem Filtrada - Laplaciano (Mascara 3)', filtered_image3)
cv2.imshow('Imagem Filtrada - Laplaciano (Mascara 4)', filtered_image4)
cv2.waitKey(0)
cv2.destroyAllWindows()
