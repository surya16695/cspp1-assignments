'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1_temp = dict1.lower()
    dict2_temp = dict2.lower()

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    input1 = input1.lower()
    input2 = input2.lower()
    print(input1)
    print(input2)

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
