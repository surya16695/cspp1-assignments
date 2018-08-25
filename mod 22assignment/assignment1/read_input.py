'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    n = int(input())
    lines = input()
    s = ""
    for i in range(n):
        for line in lines:
            s = s + str(line )
    print(s.split())
    # return s


if __name__ == '__main__':
    main()
