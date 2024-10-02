arr=[1,2,3,4,5]
tar=10
flag=False
i=0
j=len(arr)-1
while flag==False:
    if i<j:
        if arr[0]==tar:
            flag=True
            print(arr[0])
            break
        elif tar==arr[i]+arr[j]:
            flag=True
            print(arr[i],arr[j])
        elif tar>arr[i]+arr[j]:
            i+=1
        elif tar<arr[i]+arr[j]:
            j-=1
        else:
            print(-1)
            flag=True