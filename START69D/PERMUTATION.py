# cook your dish here
# cook your dish here
#! /usr/bin/env python3

T= int(input())

for i in range(0,T):
    #print("a")
    n=int(input(""))
    #print(a)
    a = input().split()
    l = [int(item) for item in a]
    
    l.sort()
    b=0
    for i in range(n):
        if l[i]>i+1:
            b=-1
            break
        else:
            b+=i-l[i]+1
    print(b)