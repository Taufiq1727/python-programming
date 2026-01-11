def sum(a,b):
    #a n=and b are local variable
    c = a+b
    z= 1#it creates a local variable called x which is destroyed after this function returns
    return c

z = 8#z is a global variable where ever it may be it prints the value of it
print(sum(4 ,6))
print(z)