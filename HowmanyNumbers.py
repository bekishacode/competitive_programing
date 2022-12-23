class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        countlist = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            countlist.append(count)
            
        return countlist
