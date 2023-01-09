class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        pairs = []
        maximum = 0
        while left <= right:
            pairs.append([nums[right], nums[left]])
            left += 1
            right -= 1
        for points in pairs:
            maximum = max(maximum, points[0] + points[1])
        return maximum
