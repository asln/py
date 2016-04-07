# Think Python Exercise 5.3
# check_fermat()

def check_fermat(a, b, c, n):
    if n < 2:
        return 'n must be greater than two'
    if a**n + b**n == c**n:
        print 'Fermat is wrong!'
    else:
        print 'No, that doesnt work'

def get_input():
    print "Checking Fermat's Last Theorem"
    a = int(input('1st number: '))
    b = int(input('2nd number: '))
    c = int(input('3rd number: '))
    n = int(input('exponential: '))
    check_fermat(a, b, c, n)

get_input()
    
