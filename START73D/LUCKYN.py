
# cook your dish here
#! /usr/bin/env python3
def abc(a):

    d=[]
    i=0
    if a<0:
        a=a*-1
    
    while a>0:
        c=a%10
        d.append(c)
        a=a//10
    #print(len(d))
    g=len(d)
    h=0
    while g>0:
        if (d[0]==7):
            h=1
        del d[0]
        g=g-1
    
        
    #print(d)
    d=[]
    if h==1:
        print("YES")
    else:
        print("NO")




T= int(input())

for __ in range(0,T):
    a=int(input())
    abc(a)
