print ("Enter three angles to examine:")
A = int(input())
B = int(input())
C = int(input())

print (A,B,C)
Isosceles = "tam giac can"
Equilateral = "tam giac deu"
Scalene = "tam giac 3 canh khac nhau"
Not_A_Triangle = "khong phai tam giac"

if A + B > C and A + C > B and B + C > A:
    if (A == B and B != C) or (B == C and C != A) or (A == C and C != B):
        print (Isosceles)
    elif A == B == C:
        print (Equilateral)
    elif A != B != C:
        print (Scalene)
else:
    print (Not_A_Triangle)