# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    len_str = len(aStr)
    if len_str == 0:
        return False
    if len_str == 1:
        return aStr == char
    if char < aStr[len_str//2]:
        return isIn(char, aStr[:len_str//2])
    elif char > aStr[len_str//2]:
        return isIn(char, aStr[len_str//2+1:])
    return True

def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__ == "__main__":
    main()