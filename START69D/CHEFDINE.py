# cook your dish here
#! /usr/bin/env python3

T= int(input())

for i in range(0,T):
    #print("a")
    #a=int(input("Enter a set:"))
    #print(a)
    a = input().split()
    l = [int(item) for item in a]
    
    n=l[0]
    k=l[1]
    
    b = input().split()
    c = [int(item) for item in b]

    q = input().split()
    time = [int(item) for item in q]
    
    
    
    d={}
    
    for i in range(n):
        if c[i] not in d.keys():
            d[c[i]]=time[i]
        else:
            d[c[i]]=min(d[c[i]],time[i])
    if len(d)<k:
        print("-1")
    else:
        m=list(d.values())
        m.sort()
        print(sum(m[:k]))