#! /usr/bin/env python3

T= int(input())
b=[]
for i in range(0,T):
    n=int(input())
    
    _ = input().split()
    a = [int(item) for item in _]
    
    _ = input().split()
    b = [int(item) for item in _]
    c=[]
    i=0
    
    for _ in range (0,n):
        if a[_]>0:
            if b[_]>0:
                i=i+1
                c.append(i)
                
            else:
                i=0
        else:
            i=0
            
    if len(c)>0:
        print(max(c))
    else:
        print(0)
        
    
    