'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    """ cleaning of string"""
    input_string = string
    regex = re.compile("[^a-zA-Z0-9]")
    input_string = regex.sub('', input_string)
    # print(input_string)
    return input_string

def main():
    """taking input string"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
