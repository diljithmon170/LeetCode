price="203"
turn=2
s=[]
s=list(str(price))
print(s)
while turn>0:
    max_no=max(s)
    s.remove(max_no)
    turn-=1
print(s)

