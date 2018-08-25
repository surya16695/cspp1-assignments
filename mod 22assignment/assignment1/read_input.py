'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''input lines'''
    no_of_lines = int(input())
    l = ""
    for i in range(no_of_lines):
        l += input()+"\n"

    print(l)

if __name__ == '__main__':
    main()
