# cook your dish here
#! /usr/bin/env python3

T= int(input())
b=[]
for i in range(0,T):
    #print("a")
    #a=int(input("Enter a set:"))
    #print(a)
    a = input().split()
    l = [int(item) for item in a]

    if l[0]+l[1]==l[2]:
        print("YES")
    elif l[1]+l[2]==l[0]:
        print("YES")
    elif l[0]+l[2]==l[1]:
        print("YES")
    else:
        print("NO")