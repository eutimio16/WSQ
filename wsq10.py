import statistics
print(" A01630244 Eutimio Machuca parra")
def fsuma (n):
    sum1 = 0
    for indice in range(len(n)):
       sum1 = sum1 + n[indice]
    return sum1
def average (n):
    a = suma / 10.0
    return a
def desviation (n):
    des = statistics.stdev(A)
    return des
x = 0
A=[]
while (x < 10):
    x = x + 1
    n = float(input("Give me a number: "))
    A.append(n)
    suma = fsuma(A)
    average2 = average(A)
desviation2 = desviation(A)
print ("Total sum: ",suma)
print ("Average: ", average2)
print ("Stardard deviation is: ", desviation2)