# cook your dish here
#! /usr/bin/env python3

T= int(input())
for i in range(0,T):
    a = input().split()
    l = [int(item) for item in a]
    b = input().split()
    m = [int(item) for item in b]
    c = input().split()
    q = [int(item) for item in c]
    
    n=l[0]
    x=l[1]
    d=0
    for i in range(0,n):
        if m[i]>=x:
            d=d+q[i]
    
    print(d)