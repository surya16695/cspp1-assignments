#define the gen_primes function here
def genPrimes():
    next = 2
    while True:
        c = 0
        for n in range(1, next+1):
            if next % n == 0 & c<4:
                c += 1
        if c == 2:
            yield next
            next += 1
        else:
            next += 1

def main():
    data = input()
    l = data.split()
    a = int(l[0])
    b = int(l[1])
    primeGenerator = genPrimes()
    for i in range(a):
        p = primeGenerator.__next__()
        if(i%b == 0):
            print(p)

if __name__ == "__main__":
    main()
