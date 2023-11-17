class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left = 0
        right = len(height)-1
        while left < right:
            hight = min(height[left],height[right])
            wight = right - left
            area = hight * wight
            max_area = max(max_area,area)

            if height[left] > height[right]:
                right -= 1
            else :
                left += 1
        return max_area
    
height = [1,8,6,2,5,4,8,3,7]
a = Solution
b = a.maxArea(a,height)
print(b)
