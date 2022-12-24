class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for j in range(len(nums)):
            for i in range(len(nums) - 1):
                if eval(nums[i]) > eval(nums[i + 1]):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums[-k]
