nums=[1,3,3,6,8]
val=3
i=0
while i<len(nums):
    if nums[i]==val:
        nums.pop(i)
    else:
        i+=1
print(nums)