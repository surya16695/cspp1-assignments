'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    # n = int(input())
    # lines = input().split()
    # s = ""
    # for i in range(n):
    #     for line in lines:
    #         s = s + str(line)
    # print(s)
    # # return s
    no_of_lines = int(input())
    lines = ""
    for i in range(no_of_lines):
        lines+=input()+"\n"

    print (lines)

if __name__ == '__main__':
    main()
