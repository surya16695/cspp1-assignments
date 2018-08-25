'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    var_dict = {}
    arg = string.split()
    for a in arg:
        if a in var_dict:
            var_dict[a]+=1;
        else:
            var_dict[a] = 1;

    return var_dict
            
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
