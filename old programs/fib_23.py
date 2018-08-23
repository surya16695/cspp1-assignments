def fib(n):
    lis_t = []
    # a = 0
    # b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        i =0
        while i<n:
            lis_t = lis_t.append(fib(n-1)+fib(n))
            i = i+1
    return lis_t
def main():
    n = 26
    number = [] 
    number = fib(n)
    print (number)

if __name__== "__main__":
    main()
