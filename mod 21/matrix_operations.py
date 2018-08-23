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
    pass

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    lis_t1 = []
    for j in m:
        lis_t = []
        for i in n:
            lis_t[i] = int(input())
        lis_t1.append(lis_t)
    return lis_t1   
def main():
    m = int(input())
    n = int(input())
    mat_1 = []
    mat_2 = []
    mat_3 = []
    # read matrix 1
    mat_1 = read_matrix(lis_t, m, n)
    print(mat_1)
    # read matrix 2
    mat_2 = read_matrix(lis_t, m, n)
    print(mat_2)
    # add matrix 1 and matrix 2
    # mat_3 = add_matrix(mat_1, mat_2)
    # print(mat_3)
    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
