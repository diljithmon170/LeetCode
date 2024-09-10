nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
n1=[]
n2=[]
m=3
n=3
if m>0:
    for i in range(m):
        n1.append(nums1[i])
if n>0:
    for j in range(n):
        n2.append(nums2[j])
print("n1=",n1)
print("n2=",n2)

if m==0:
    nums1=n2
elif n==0:
    nums1=n1
else:
    merge=n1+n2
    nums1=sorted(merge)
print(nums1)


# idx = m + n - 1
# while m > 0 and n > 0:
#     if nums1[m - 1] < nums2[n - 1]:
#         nums1[idx] = nums2[n - 1]
#         n -= 1
#     else:
#         nums1[idx] = nums1[m - 1]
#         m -= 1
#     idx -= 1
# while n > 0:
#     nums1[idx] = nums2[n - 1]
#     n -= 1
#     idx -= 1