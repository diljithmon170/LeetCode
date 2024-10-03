arr=[2,3,5,6,4,7,0,11]
tar=8
dict1={}
for i in range(len(arr)):
    dict1[arr[i]]=i
print(dict1)
for i in range(len(arr)):
    t_sum=abs(arr[i]-tar)
    if t_sum in dict1.keys():
        print(i,dict1[t_sum])
    print()