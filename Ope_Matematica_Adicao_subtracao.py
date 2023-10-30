#Aluno: Lucas Carvalho da Luz Moura
import cv2
import numpy as np

# Carregamento das duas imagens
imagem1 = cv2.imread('/home/lucasmoura/Downloads/PI1.jpg')
imagem2 = cv2.imread('/home/lucasmoura/Downloads/PI1.jpg')

# Verificando se as imagens foram carregadas
if imagem1 is None or imagem2 is None:
    print('Erro ao carregar as imagens.')
else:
    # Certificando se as duas imagens tem o mesmo tamanho
    if imagem1.shape == imagem2.shape:
        # Fazendo a Soma das duas imagens
        soma = cv2.add(imagem1, imagem2)

        # Subtraindo a segunda imagem pela primeira
        subtracao = cv2.subtract(imagem1, imagem2)

        # Mostrar as imagens originais e os resultados
        cv2.imshow('Imagem 1', imagem1)
        cv2.imshow('Imagem 2', imagem2)
        cv2.imshow('Soma', soma)
        cv2.imshow('Subtracao', subtracao)

        # Aguardando até que uma tecla seja pressionada e feche as janelas
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print('As imagens não têm o mesmo tamanho.')
