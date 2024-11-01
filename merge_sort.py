list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
i=j=0
merge_sort=[]
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        merge_sort.append(list1)
        i+=1
    else:
        merge_sort.append(list2)
        i+=1
while i<len(list1):
    merge_sort.append(list1[i])
    i+=1
while j<len(list2):
    merge_sort.append(list1[j])
    j+=1
res=merge_sort
print(" ".join(map(str, res)))