# cook your dish here
T= int(input(""))
for i in range(0,T):
    n=int(input())
    m=input()
    l=list(map(int, str(m)))
    sum=0
    for i in l:
        if i==1:
            sum +=1
    if m=="1" or m=="10":
        print("NO")
    elif sum <=3:
        print("YES")
    else:
        print("NO")