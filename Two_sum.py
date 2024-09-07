List=[2,7,11,15]
tar=9
for i in range(len(List)):
    for j in range(i+1,len(List)):
        if List[i]+List[j]==tar:
            print(i,j)

""" class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return[i,j] """