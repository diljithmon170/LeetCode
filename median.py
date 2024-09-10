num1=[1,3]
num2=[2,4]
merge=num1+num2
merge_arr=sorted(merge)
print(merge_arr)
l=len(merge)
if l%2!=0:
    m=(int(l/2))
    print("median=", merge_arr[m])
else:
    m=(int(l/2)-1)
    print("median=", (merge_arr[m]+merge_arr[m+1])/2)