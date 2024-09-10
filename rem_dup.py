nums=[1,3,3,6,8]
i=1
while i<len(nums):
    if nums[i]==nums[i-1]:
        nums.pop(i)
    else:
        i+=1
print(nums)