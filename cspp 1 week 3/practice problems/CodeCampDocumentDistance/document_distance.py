'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    word_stop = load_stopwords('stopwords.txt')
    input_1 = []
    input_2 = []
    input_1 = input1.lower()
    input_2 = input2.lower()
    dict1 = {}
    dict2 = {}
    input_1 = input_1.strip().replace('.', '').replace(',', '').replace('?', '').split()
    #print(input_1)
    input_2 = input_2.strip().replace('.', '').replace(',', '').replace('?', '').split()
    #print(input_2)
    # dict1 = make_dict(input_1)
    # dict2 = make_dict(input_2)
    # dict_temp1 = {}
    # dict_temp2 = {}
    # stop_words = load_stopwords(r)
    # dict_temp1 = del.dict1[stop_words]
    # print(dict_temp1)
    # dict_temp2 = del.dict2[stop_words]
    # print(dict_temp2)
    input_up1 = []
    input_up2 = []
    input_up1 = input_1 - word_stop
    print(input_1)
    input_up2 = input_2 - word_stop
    print(input_2)

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
    return dict_1
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
