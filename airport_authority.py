n=4
weights=[1,2,3,4]
t=3
pay=0
for i in range(n):
    if weights[i]<=t:
        pay+=1
    else:
        pay+=2
print(pay)

