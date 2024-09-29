num=4
no=4
flag=True
for i in range(10,15):
    x=i
    s=""
    s+=str(i)
    p=int(s[0])+int(s[1])
    if p>1:
        for i in range(2,(p//2)+1):
            if p%i==0:
                flag=False
                break
            else:
                flag=True
        if flag==True:
            y=x
print(y)


