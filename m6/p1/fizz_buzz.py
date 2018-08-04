'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
NUM = int(input())
I = 1
while I <= NUM:
    if I%3 == 0:
        print("Fizz")
    elif I%5 == 0:
        print("Buzz")
    else:
        print(I)
    I = I+1
print("required output is acquired")
   