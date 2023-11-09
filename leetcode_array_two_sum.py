class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num = {}
        long = len(nums)
        for i in range(long) :
            if nums[i] not in num :
                num[target-nums[i]] = i
            else :
                return [num[nums[i]],i] 
        
           
nums = [3,2,4]
target = 6
a = Solution
b = a.twoSum(a,nums,target)
print(b)