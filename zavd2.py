import numpy as np

def create_matrix(n):
    return np.random.randint(1, 13, size=(n, n))

def calculate_diagonal_product(matrix):
    return np.prod(np.diag(matrix))

def replace_duplicates(matrix):
    unique_elements = set()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] in unique_elements:
                matrix[i, j] = 0
            else:
                unique_elements.add(matrix[i, j])
    return matrix

def main():
    N = int(input("Введіть розмір матриці N: "))
    matrix = create_matrix(N)
    print("Матриця:")
    print(matrix)

    diagonal_product = calculate_diagonal_product(matrix)
    print(f"Добуток елементів на головній діагоналі: {diagonal_product}")

    matrix_without_duplicates = replace_duplicates(matrix)
    print("Матриця після видалення повторів:")
    print(matrix_without_duplicates)

if __name__ == "__main__":
    main()