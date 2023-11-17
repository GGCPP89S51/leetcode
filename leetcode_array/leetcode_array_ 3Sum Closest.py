class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        Sum = float('inf')
        new_sum = 0
        
        for i in range(n-2):
            left,right = i+1,n-1
            
            while(left < right):
                new_sum = nums[i]+nums[left]+nums[right]
                if abs(new_sum - target) < abs(Sum - target):
                    Sum = new_sum

                if new_sum < target:
                    left += 1
                elif new_sum > target:
                    right -= 1
                else:
                    return new_sum

        return Sum

nums = [-1,2,1,-4]
target = 1
a = Solution
b = a.threeSumClosest(a,nums,target)
print(b)