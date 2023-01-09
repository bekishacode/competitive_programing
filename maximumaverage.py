class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximumAverage = -float('inf')
        average = 0
        currentSum = 0
        for currentIndex in range(len(nums)):
            currentSum += nums[currentIndex]
            if(currentIndex >= k - 1):
                 average = currentSum / k
                 maximumAverage = max(maximumAverage, average) 
                 currentSum -= nums[currentIndex - (k - 1)]
        return maximumAverage
