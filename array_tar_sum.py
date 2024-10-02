def sum(arr,tar):
    l=r=0,len(arr)-1
    while l<r:
        temp_sum=arr[l]+arr[r]
        if temp_sum==tar:
            return (arr[l],arr[r])
        elif temp_sum<tar:
            l+=1
        else:
            r+=1
    return -1

arr=[1,4,8]
tar=9
result=sum(arr,tar)
if result:
    print(result)
else:
    print("not found")