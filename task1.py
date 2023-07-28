# Напишите функцию для транспонирования матрицы

my_matrix = [[1, 2, 3], [4, 5, 6]]

def transp (matrix: list[list[int]]):
    temp = []
    for i in range(len(matrix[0])):
        temp.append([])
        for j in range(len(matrix)):
            temp[i].append(matrix[j][i])
    return temp

print(transp(my_matrix))