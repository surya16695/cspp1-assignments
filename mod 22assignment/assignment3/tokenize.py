'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re

def tokenize(string):
	"""tokenize strings"""
    dic_t = {}
    # s = ""
    input_string = string    
    regex = re.compile("[^a-zA-Z0-9]")
    input_string = regex.sub('', input_string)
    s = input_string.split(" ")[:-1]
    for word in s:
        if word not in dic_t:
            dic_t[word] = string.count(word) 
    return dic_t
    
def main():
    n = int(input())
    l_1 = ""
    for i in range(n):
        l_1 += input()
        i = i+1
    # print(l_1)
    print(tokenize(l_1.split()))
if __name__ == '__main__':
    main()
