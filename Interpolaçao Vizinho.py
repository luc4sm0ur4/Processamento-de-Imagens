#Aluno: Lucas Carvalho da Luz Moura

import numpy as np

def nearest_neighbor_reduction(data, new_shape):
    # Parte que calcula as proporções para redimensionamento
    row_ratio = data.shape[0] / new_shape[0]
    col_ratio = data.shape[1] / new_shape[1]

    # Parte que gera índices para os novos dados interpolados
    new_rows, new_cols = np.meshgrid(np.arange(new_shape[0]), np.arange(new_shape[1]))
    
    # Parte que calcula os índices correspondentes nos dados originais
    orig_rows = np.floor(new_rows * row_ratio).astype(int)
    orig_cols = np.floor(new_cols * col_ratio).astype(int)
    
    # Extrai os valores dos dados originais usando os índices calculados
    new_data = data[orig_rows, orig_cols]
    
    return new_data

def nearest_neighbor_expansion(data, new_shape):
    # Calcula as proporções para redimensionamento
    row_ratio = data.shape[0] / new_shape[0]
    col_ratio = data.shape[1] / new_shape[1]

    # Gera índices para os novos dados interpolados
    new_rows, new_cols = np.meshgrid(np.arange(new_shape[0]), np.arange(new_shape[1]))

    # Calcula os índices correspondentes nos dados originais
    orig_rows = np.floor(new_rows * row_ratio).astype(int)
    orig_cols = np.floor(new_cols * col_ratio).astype(int)
    
    # Extrai os valores dos dados originais usando os índices calculados
    new_data = data[orig_rows, orig_cols]
    
    return new_data

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_data_reduced = nearest_neighbor_reduction(data, (2, 2))
new_data_expanded = nearest_neighbor_expansion(data, (4, 4))

print('\nNovo dado da Interpolação por redução \n')
print(new_data_reduced)
print('\nNovo dado da Interpolação por ampliação \n')
print(new_data_expanded)