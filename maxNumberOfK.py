class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        maxNumberOfOperation = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            currentSum = nums[left] + nums[right]
            if currentSum == k:
                maxNumberOfOperation += 1
                right -= 1
                left += 1
            elif currentSum > k:
                right -= 1
            else:
                left +=1       
        return maxNumberOfOperation
