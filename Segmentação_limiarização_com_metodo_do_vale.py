#Aluno: Lucas Carvalho da Luz Moura
#Matricula: 2020111816

import cv2
import numpy as np

def Segmentacao_Limiar(image, threshold):
 
  segmented_image = np.zeros_like(image)
  segmented_image[image >= threshold] = 1
  
  return segmented_image

def Limiar_Vale(image):
  histogram = np.histogram(image, 256, (0, 255))[0]
  valley_threshold = (histogram[0] + histogram[1]) / 2
  
  return valley_threshold

def main():
  
  image = cv2.imread("/home/lucasmoura/Área de trabalho/Projetos/Códigos para gravação/PI1.jpg", 1)
  threshold = Limiar_Vale(image)
  segmented_image = Segmentacao_Limiar(image, threshold)

  cv2.imshow("Imagem Original", image)
  cv2.imshow("Imagem com Limiariazacao e com Metodo do Vale", segmented_image)
  cv2.waitKey(0)

if __name__ == "__main__":
  main()
