x=-900000
r=""
m="-"
s=str(x)
if s[0]=="0":
    r="0"
if s[0]=="-" and s[-1]!="0":
    r+=m
    for i in range(len(s)-1,0,-1):
        r+=s[i]

if s[-1]=="0" and s[0]!="-":
    for i in range(len(s)-1,-1,-1):
        if s[i]!="0":
            r+=s[i]

if s[0]!="-" and s[-1]!="0":
    for i in range(len(s)-1,-1,-1):
        r+=s[i]

if s[0]=="-" and s[-1]=="0":
    r="-"+s[1]
x=int(r)
print(x)