def zigzag(s,numrows):
    if numrows==1 or numrows>=len(s):
        return s
    rows=[[] for _ in range(numrows)]
    idx,d=0,1
    for char in s:
        rows[idx].append(char)
        if idx==0:
            d=1
        elif idx==numrows-1:
            d=-1
        idx+=d
    for i in range(numrows):
        rows[i]=''.join(rows[i])
       
    return ''.join(rows)

s="QWERTYUIPO"
numrows=3
print(s)
print(zigzag(s,numrows))
