T= int(input(""))
for i in range(0,T):
    a = input("").split()
    l = [int(item) for item in a]
    print(l[1]//l[0])