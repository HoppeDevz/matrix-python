old_matrix = [
    [4, 7, 9, 8],
    [6, 3, 2, 1],
    [9, 3, 2, 2],
    [1, 1, 3, 4]
]

matrix = [
    [4, 7, 9, 8],
    [6, 3, 2, 1],
    [9, 3, 2, 2],
    [1, 1, 3, 4]
]

def AppendFirstAndSecondColumn(Matrix):
    _matrix = Matrix

    fc_index = 0
    first_column = []

    sc_index = 0
    second_column = []

    # make a first column
    for i in _matrix:
        # i => row => 0~3
        first_column.insert(fc_index, i[0])
        fc_index = fc_index + 1

    # make a second column
    for i in _matrix:
        # i => row => 0~3
        second_column.insert(sc_index, i[1])
        sc_index = sc_index + 1
    
    app_fc_index = 0
    # append a first column
    for k in _matrix:
        k.append(first_column[app_fc_index])
        app_fc_index = app_fc_index + 1

    app_sc_index = 0
    # append a first column
    for k in _matrix:
        k.append(second_column[app_sc_index])
        app_sc_index = app_sc_index + 1

    for k in _matrix:
        print(str(k) + "\n")

    return _matrix

def CalculateDeterminant(formated_matrix, old_matrix):
    # f(x) => x - 1 => x = matrix column length
    arrow_length = len(old_matrix[0]) - 1
    column_length = len(formated_matrix)

    principal_diagonal = []
    secondary_diagonal = []
    
    #make a first diagonal
    for k in range(0, arrow_length):
        arr = []
        for j in range(0, column_length):
            arr.append(formated_matrix[j][j + k])

        principal_diagonal.append(arr)

    #make a secondary diagonal
    for k in range(0, arrow_length):
        arr = []
        for j in range(0, column_length):
            arr.append(formated_matrix[j][(arrow_length + 2) - (j + k) ])

        secondary_diagonal.append(arr)

    sum_first_diagonal = 0
    sum_second_diagonal = 0

    for k in principal_diagonal:
        p = 1
        for j in k:
            p = p * j
        
        sum_first_diagonal = sum_first_diagonal + p

    for k in secondary_diagonal:
        p = 1
        for j in k:
            p = p * j
        
        sum_second_diagonal = sum_second_diagonal + p
    
    # RESULT
    print(sum_first_diagonal - sum_second_diagonal)
        


CalculateDeterminant(AppendFirstAndSecondColumn(matrix), old_matrix)


