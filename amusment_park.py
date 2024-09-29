price="2500"
turn=2
s=[]
t=[]
s=list(str(price))
t=list(str(price))
print(s)
while turn>0:
    max_no=max(t)
    t.remove(max_no)
    z=t.count('0')
    print(z)
    if z==len(t):
        s.remove('0')
    else:
        max_no=max(s)
        s.remove(max_no)
    turn-=1
print(s)

