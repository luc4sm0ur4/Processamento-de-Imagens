#Aluno: Lucas Carvalho da Luz Moura

import numpy as np

def bilinear_reduction(data, new_shape):
    orig_height, orig_width = data.shape
    new_height, new_width = new_shape
    row_ratio = orig_height / new_height
    col_ratio = orig_width / new_width

    new_data = np.empty(new_shape)

    for i in range(new_height):
        for j in range(new_width):
            orig_i, orig_j = i * row_ratio, j * col_ratio
            i_floor, j_floor = int(orig_i), int(orig_j)
            i_ceil, j_ceil = min(i_floor + 1, orig_height - 1), min(j_floor + 1, orig_width - 1)
            alpha, beta = orig_i - i_floor, orig_j - j_floor

            new_data[i, j] = (1 - alpha) * ((1 - beta) * data[i_floor, j_floor] + beta * data[i_floor, j_ceil]) + \
                             alpha * ((1 - beta) * data[i_ceil, j_floor] + beta * data[i_ceil, j_ceil])

    return new_data

def bilinear_expansion(data, new_shape):
    orig_height, orig_width = data.shape
    new_height, new_width = new_shape
    row_ratio = orig_height / new_height
    col_ratio = orig_width / new_width

    new_data = np.empty(new_shape)

    for i in range(new_height):
        for j in range(new_width):
            orig_i, orig_j = i * row_ratio, j * col_ratio
            i_floor, j_floor = int(orig_i), int(orig_j)
            i_ceil, j_ceil = min(i_floor + 1, orig_height - 1), min(j_floor + 1, orig_width - 1)
            alpha, beta = orig_i - i_floor, orig_j - j_floor

            new_data[i, j] = (1 - alpha) * ((1 - beta) * data[i_floor, j_floor] + beta * data[i_floor, j_ceil]) + \
                             alpha * ((1 - beta) * data[i_ceil, j_floor] + beta * data[i_ceil, j_ceil])

    return new_data

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_data_reduced = bilinear_reduction(data, (2, 2))
new_data_expanded = bilinear_expansion(data, (4, 4))

print('\nNovo dado da Interpolação Bilinear por redução \n')
print(new_data_reduced)
print('\nNovo dado da Interpolação Bilinear por ampliação \n')
print(new_data_expanded)
