#Aluno: Lucas Carvalho da Luz Moura
import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread("/run/media/lucasmoura/a89d1316-f206-4962-b8a0-f489e3a254dc/Backup Arquivos/Processamento de Imagens 2023/Cinza.jpg", cv2.IMREAD_GRAYSCALE)

# Criacao do kernel da dilatação
kernel = np.ones((3, 3), np.uint8)

# Aplica a dilatação na imagem original
dilation = cv2.dilate(img, kernel, iterations=1)

# Criacao do kernel da erosão
kernel = np.ones((3, 3), np.uint8)

# Aplica a erosão na imagem original
erosion = cv2.erode(img, kernel, iterations=1)

# Calculo do gradiente morfológico
gradient = dilation - erosion

# Exibição da imagem original e gradiente
cv2.imshow("Original", img)
cv2.imshow("Gradiente", gradient)
cv2.waitKey(0)