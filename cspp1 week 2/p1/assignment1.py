# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes
#in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def fact_orial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    """doc string"""
    if n <= 1:
        return 1
    else:
        return n*fact_orial(n-1)
    pass
""" def calling the function"""
def main():
    a_1 = input()
    print(fact_orial(int(a_1)))    

if __name__ == "__main__":
    main()
