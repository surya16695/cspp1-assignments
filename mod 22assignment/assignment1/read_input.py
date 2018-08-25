'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''input lines'''
    no_of_lines = int(input())
    l_1 = ""
    for i in range(no_of_lines):
        l_1 += input()+"\n"

    print(l_1)

if __name__ == '__main__':
    main()
