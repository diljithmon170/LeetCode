n=int(input())
m=int(input())
diff=0
for i in range(n,m):
    l1=[]
    l1.append(str((i)))
    j=0
    s=""
    for k in range(len(l1)):
        s+=l1[k]
    for j in range(len(s)-1):
        if j+1<len(s):
            diff=abs(int(s[int(j)])-int(s[int(j+1)]))
    if diff==1:
        print(s,end=" ")

# num=input()
# l1=[]
# l1=list(map(int,num.split(" ")))
# print(l1)