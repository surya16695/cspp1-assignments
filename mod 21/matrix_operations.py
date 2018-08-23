def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        sum = []
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                sum.append(m1[i][j] + m2[i][j])
        return sum
    return print("Error: Matrix shapes invalid for addition")

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    line = input().split(',')
    m = int(line[0])
    n = int(line[1])
    print(line)
    lis_t = []
    for j in range(m):
        lis_t.append([int(i) for i in input().split()])
    for i in range(0, len(lis_t)-1):
        if len(lis_t[i]) != n:
            return print("Error: Invalid input for the matrix")
    return lis_t


def main():
    mat_1 = []
    mat_2 = []
    mat_3 = []
    # read matrix 1
    mat_1 = read_matrix()
    print(mat_1)
    # read matrix 2
    mat_2 = read_matrix()
    print(mat_2)
    # add matrix 1 and matrix 2
    mat_3 = add_matrix(mat_1, mat_2)
    print(mat_3)
    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
