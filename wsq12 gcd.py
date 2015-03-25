__author__ = 'Eutimio'
Print("Eutimio machuca parra A01630244")
def gcd(x,y):
    if (x==y):
        ans=x
    elif(x>y):
        ans=gcd((x-y),y)
    else:
        ans=gcd(x,(y-x))
    return ans
print("this program will show you the Greatest Common Divisor of two numbers")
a=int(input("give me the first number: "))
b=int(input("give me the second number: "))
rgcd= gcd(a,b)
print("the Greatest Common Divisor of ", a, " and ", b, " is: ", rgcd)
def gcd(x,y):
    if (x==y):
        ans=x
    elif(x>y):
        ans=gcd((x-y),y)
    else:
        ans=gcd(x,(y-x))
    return ans
