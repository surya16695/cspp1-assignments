'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    n = int(input())
    s = ""
    lines = input()
    for i in range(n):
        for line in lines:
            s = s + str(line "\n")
    # for i in range(len(s)):
    print(s)
    # return s


if __name__ == '__main__':
    main()
