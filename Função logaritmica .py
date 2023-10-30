#Aluno: Lucas Carvalho da Luz Moura

import cv2
import numpy as np

def log_transform(image, factor=1):

  # Converter a imagem para um array numpy.
  image = np.array(image)

  # Aplicar a transformação logaritmica.
  image = np.log(image + 1) * factor

  # Limitar os valores de intensidade resultantes ao intervalo [0, 255].
  image = np.clip(image, 0, 255)

  # Converter a imagem de volta para um objeto OpenCV.
  image = cv2.cvtColor(image.astype("uint8"), cv2.IMREAD_COLOR)

  return image


# Carregar a imagem original.
image = cv2.imread('/home/lucasmoura/Downloads/PI1.jpg', cv2.IMREAD_COLOR)

# Aplicar a transformação logaritmica.
image_log = log_transform(image)

# Exibir as imagens original e transformada.
cv2.imshow("Imagem original", image)
cv2.imshow("Imagem transformada", image_log)
cv2.waitKey(0)
cv2.destroyAllWindows()
