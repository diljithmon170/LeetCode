arr=[3,3,4,2,4,4,2,4,4]
len_half=len(arr)/2
print(len_half)
for i in arr:
    if(arr.count(i)>len_half):
        ele=i
        flag=True
if not flag:
    print(-1)
else:
    print(ele)
    