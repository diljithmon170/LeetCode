a=[23,25,7,8,9]
max_val=max(a)
b=[]
for i in range(max_val):
    if i*i<=max_val:
        b.append(i*i)
for i in a:
    if i in b:
        print(i)