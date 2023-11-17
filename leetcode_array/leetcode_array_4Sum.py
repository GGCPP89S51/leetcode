class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n-3) :
            for j in range(i + 1, n - 2):
                left ,right = j+1 ,n -1
                while left<right:
                    cur_sum = nums[i]+nums[left]+nums[right]+nums[j]
                    if cur_sum == target :
                        if [nums[i],nums[left],nums[right],nums[j]] not in result:
                            result.append([nums[i],nums[left],nums[right],nums[j]])
                        left += 1 
                        right -= 1 
                    elif cur_sum < target:
                        left += 1
                    else:
                        right -= 1
        return result
    
nums = [-3,-1,0,2,4,5]
target = 2
a = Solution
b = a.fourSum(a,nums,target)
print(b)    