class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n-1) :
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1

            while(left < right):
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0 :
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1
        return result

nums = [-1,0,1,2,-1,-4]
a = Solution
b = a.threeSum(a,nums)
print(b)