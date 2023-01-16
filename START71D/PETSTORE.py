#! /usr/bin/env python3

T= int(input())

for i in range(0,T):
    a=int(input())
    _ = input().split()
    l = [int(item) for item in _]
    s=list(set(l))
    i="YES"

    for _ in range(len(s)):
        
        if l.count(s[_])%2 != 0:
            i="NO"
            break
    print(i)