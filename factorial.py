def Factorial():
    fac = input("Enter a number: ")
    i = fac-1
    while i > 0:
        fac = fac * i
        i = i-1
    return fac
    
Factorial()
