x=1213
s=str(x)
le=len(s)
flag="true"
first=0
last=le-1
while(first<last):
    if s[first]!=s[last]:
        flag="false"
    first+=1
    last-=1
print(flag)
