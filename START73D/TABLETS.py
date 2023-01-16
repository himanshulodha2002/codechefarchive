# cook your dish here
#! /usr/bin/env python3

T= int(input())

for i in range(0,T):
    a = input().split()
    l = [int(item) for item in a]
    
    if(3*l[0]<=l[1]):
        print("YES")
    else:
        print("NO")
        