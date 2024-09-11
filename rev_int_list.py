x=-123000
s=str(x)
rv=s[::-1]
l=list(rv)
print(rv)
print(l)
i=0
while i < len(l):
    if l[i] == '0':
        l.pop(i)
        break
print(l)
# l=list(s)
# r=[]
# r=l.reverse(s)
# print(l)
# print(r)