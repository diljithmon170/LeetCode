s="absccfghnmg"

# s=set(s)
# return len(s)
if len(s)==0:
    print(0)
i=0
j=0
seen=set()
max_count=0

while j<len(s):
    if s[j] not in seen:
        seen.add(s[j])
        j+=1
        max_count=max(max_count,j-i)
    else:
        while s[i]!=s[j]:
            seen.remove(s[i])
            i+=1
        seen.remove(s[i])
        i+=1
print(max_count)   