#! /usr/bin/env python3

T= int(input())
for i in range(0,T):
    a=int(input())
    b = input()#.split()
    #l = [int(item) for item in b]
    l=[]
    for i in range (a):
        if b[i]=='1':
            l.append(i)
            
    q=len(l)
    for i in range(1,q):
        m=l[i]
        o=l[i-1]
        if(m-o)%2!=0:
            print(1)
            break
    else:
        print(2)
