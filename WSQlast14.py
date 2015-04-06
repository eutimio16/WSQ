__author__ = 'Eutimio'
print(" Eutimio machuca parra", " A1630244")
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
n=(int(input(print("give me a number to factorize"))))
def constate_e(p):
    e = 0
    for n in range(100):
        last = e
        e = e + 1.0 / factorial(n)
        print("ahora estimamos",e,"iteracion",n)
        if(False):
            break
    return e

p = int(input("give precision"))
e = constate_e(p)
print(e)