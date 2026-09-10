class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        totalD: int = 0
        for i in nums:
            for j in str(i):
                totalD += int(j)
        return sum(nums)-totalD