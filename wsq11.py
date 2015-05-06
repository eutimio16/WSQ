#WSQ11 Eutimio MAchuca parra A01630244
def palindromes(x):
    x1 = str(x)
    x2 = x1[::-1]
    x3 = int(x2)
    if(x==x3):
        return True
    else:
        return False
palindrome = 0
nonlychrels = 0
Lychrels = 0

x = int(input("Give me the LOWER bound of numbers to consider: "))
y = int(input("Give me the UPPER bound of numbers to consider: "))
print("And the reslts are for the range",x, "to",y)
for c in range(x,y+1):
    c1 = palindromes(c)
    if(c1==False):
        c2 = 0
        p1 = False
        candidate = c
        while(c2<30 and p1==False):
            c2 = c2 + 1
            c3 = str(candidate)
            r = c3[::-1]
            r1 = int(r)
            candidate += + r1
            p1 = palindromes(candidate)
        if(p1==True):
            nonlychrels += + 1
        if(c2==30 and p1==False):

            Lychrels += + 1

    else:
        palindrome+= + 1
print("Natural Palindromes: ", palindrome)
print("Non Lychrel (become palindrome): ", nonlychrels)
print("Lychrel candidates : ", Lychrels)