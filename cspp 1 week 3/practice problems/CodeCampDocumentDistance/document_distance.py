'''
    Document Distance - A detailed description is given in the PDF
'''
import re

def clean(input_string):
    input_string = input_string.lower()
    regex = re.compile('(^a-z)')
    input_string = regex.sub('', input_string)
    return input_string


def computation(dict):
    numerator = sum(values[0]*values[1] for value in dict.values())
    denoinator1 = math.sqrt(sum(value[0]**2 for value in dict.values()))
    denoinator2 = math.sqrt(sum(value[0]**2 for value in dict.values()))
    return (numerator/(denominator1*denominator2))

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    #dict1 = make_dict(input_1)
    #dict2 = make_dict(input_2)
    #dict1 = dict1.strip().replace('.', '').replace(',', '').replace('?', '').split()
    #print(input_1)
    #dict2 = dict2.strip().replace('.', '').replace(',', '').replace('?', '').split()
    #print(input_2)
    dict1 = clean(dict1)
    dict2 = clean(dict2)
    dict_1 = make_dict(dict1)
    dict_2 = make_dict(dict2)
    word_stop = load_stopwords('stopwords.txt')
    # dict_temp1 = Delete(dict_1, word_stop)
    # dict_temp2 = Delete(dict_2, word_stop)
    dict_temp3 = adding(dict_1, dict_2)
    return computation(dict_temp3)

    
def adding(dict1, dict2):
    dict_t = {}
    for word in dict1:
        if word in dict2:
            dict_t[word] = [dict1.get(word), dict2.get(word)] 
    return dict_t


# def Delete(dict_a, dict_b):
#     for word in dict_a:
#         if word in dict_b:
#             del dict_a[word]
#     return dict_a


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
    dict_A = {}
    word_stop = load_stopwords('stopwords.txt')
    #print(word_stop)
    for word in input:
        if word not in word_stop:
            if word not in dict_A:
                dict_A[word] = 1
            else:
                dict_A[word] += 1
    print(dict_A)
    return dict_A
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
