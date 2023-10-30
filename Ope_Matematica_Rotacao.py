#Aluno: Lucas Carvalho da Luz Moura
import cv2
import numpy as np

# Carregando a imagem
imagem = cv2.imread('/home/lucasmoura/Downloads/PI1.jpg')

# Definindo o ângulo de rotação (em graus)
angulo_rotacao = 45

# Calculando o centro da imagem
altura, largura = imagem.shape[:2]
centro = (largura // 2, altura // 2)

# Criando uma matriz de rotação
matriz_rotacao = cv2.getRotationMatrix2D(centro, angulo_rotacao, 1.0)

# Aplicando a rotação à imagem
imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao, (largura, altura))

# Exibindo a imagem original e a imagem rotacionada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Rotacionada', imagem_rotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()