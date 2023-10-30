#Lucas Carvalho da Luz Moura
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregando a imagem em escala de cinza
image = cv2.imread('/run/media/lucasmoura/a89d1316-f206-4962-b8a0-f489e3a254dc/Backup Arquivos/Processamento de Imagens 2023/Bob.jpg', cv2.IMREAD_GRAYSCALE)

# Calculando o histograma da imagem original
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Equalizando o histograma
equ = cv2.equalizeHist(image)

# Calculando o histograma da imagem equalizada
hist_equ = cv2.calcHist([equ], [0], None, [256], [0, 256])

# Criando um gráfico para mostrar os histogramas
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(hist, color='black')
plt.title('Histograma Original')
plt.subplot(2, 1, 2)
plt.plot(hist_equ, color='black')
plt.title('Histograma Equalizado')

# Salvando o gráfico como uma imagem
plt.savefig('/home/lucasmoura/Área de trabalho/histogramas.png')

# Imprimindo uma mensagem indicando que o gráfico foi salvo
print("Gráfico salvo como 'histogramas.png'")
