T= int(input())
for i in range(0,T):
    S=input()
    S1=input()

    c=[0,0]
    for i in S:
        c[int(i)]= c[int(i)] + 1
    for i in S1:
        c[int(i)]= c[int(i)] + 1
    r='1'*min(c)
    r= r + '0'*(len(S)-min(c))
    print(r)
