# Exercise:""" Assignment-1"""
# Write a Python function, factorial(n), that takes
#in one number and returns the factorial of given number.

# This function takes in one number and returns one number.

"""doc string about the factorial function"""
def fact_orial(n_1):
    '''
    n_1 is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
        if n_1 <= 1:
        return 1
    return n_1*fact_orial(n_1 - 1)

""" def calling the function"""
def main():
    a_1 = input()
    print(fact_orial(int(a_1)))    

if __name__ == "__main__":
    main()
