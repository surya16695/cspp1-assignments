"""Exercise: Assignment-2
 Write a Python function, sumofdigits, that
 takes in one number and returns the sum of digits of given number.

 This function takes in one number and returns one number.
"""
def sumofdigits(n_input):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if n_input == 0:
        return 0
    return (n_input % 10)+sumofdigits(n_input // 10)
def main():
    """def"""
    a_input = input()
    print(sumofdigits(int(a_input)))
if __name__ == "__main__":
    main()
