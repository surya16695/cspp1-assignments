'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    input_string = string
    regex = re.compile("[^a-z A-Z 0-9]")
    input_string = regex.sub('', input_string)
    # print(input_string)
    return input_string

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
