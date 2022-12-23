class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        findindices = []
        for i in range(len(nums)):
            if nums[i] == target:
                findindices.append(i)
        return findindices
