# cook your dish here
#! /usr/bin/env python3

T= int(input())
for i in range(0,T):
    a = input().split()
    l = [int(item) for item in a]

    if l[0]!=l[1] and l[1]!=l[2] and l[0]!=l[2]:
        print("YES")
    
    else:
        print("NO")