'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    #dict1 = make_dict(input_1)
    #dict2 = make_dict(input_2)
    dict_1 = []
    dict_2 = []
    word_stop = load_stopwords('stopwords.txt')
    dict_1 = dict1 - word_stop
    print(dict_1)
    dict_2 = dict2 - word_stop
    print(dict_2)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords
def make_dict(input):
    dict_1 = {}
    for word in input:
        if word not in dict_1:
            dict_1[word] = 1
        else:
            dict_1[word] += 1
    #print(dict_1)
    return dict_1
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    input_1 = input1.lower()
    input_2 = input2.lower()
    print(similarity(input_1, input_2))

if __name__ == '__main__':
    main()
