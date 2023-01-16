# cook your dish here
from math import *


T= int(input(""))
for i in range(0,T):
    
    m=int(input())
    
    a = input("").split()
    l = [int(item) for item in a]
    
    b=l[0]
    for i in l:
        b=gcd(b,i)
        
    for i in l:
        print(i//b,end=" ")
    print()
    
