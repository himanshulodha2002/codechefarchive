T= int(input(""))
for i in range(0,T):
    #print("a")
    #a=int(input("Enter a set:"))
    #print(a)
    a = input("").split()
    l = [int(item) for item in a]
    
    b=2*l[1]

    if l[0]>b:
        print("YES")
    elif l[0]<b:
        print("NO")
    elif l[0]==b:
        print("YES")
