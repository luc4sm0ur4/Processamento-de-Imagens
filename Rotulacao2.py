#Lucas Carvalho da Luz Moura
import numpy as np

WHITE = 1
BLACK = 0

di = [-1, 0, 1, 0]  # Deslocamento na direção vertical
dj = [0, 1, 0, -1]  # Deslocamento na direção horizontal

def label_image(image, connectivity=4):
    # Inicialize uma matriz de rótulos com um valor inicial.
    labels = np.full(image.shape, -1, dtype=np.int32)

    # Inicialize um contador de rótulos.
    label_count = 0

    # Percorra a imagem.
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Se o pixel estiver branco, inicie uma nova região.
            if image[i, j] == WHITE:
                labels[i, j] = label_count
                label_count += 1

            # Percorra os vizinhos do pixel.
            for n in range(connectivity):
                ni, nj = i + di[n], j + dj[n]

                # Se o vizinho estiver dentro da imagem e tiver o mesmo rótulo, atualize o rótulo do pixel.
                if 0 <= ni < image.shape[0] and 0 <= nj < image.shape[1] and labels[ni, nj] == labels[i, j]:
                    labels[i, j] = labels[ni, nj]

    return labels

# Crie uma imagem binária.
image = np.array([[WHITE, WHITE, WHITE, BLACK],
                  [WHITE, BLACK, BLACK, WHITE],
                  [WHITE, WHITE, WHITE, WHITE],
                  [BLACK, BLACK, WHITE, WHITE]])

# Rótula a imagem.
labels = label_image(image)

# Imprima os rótulos.
print('\nSaida: \n')
print(labels)