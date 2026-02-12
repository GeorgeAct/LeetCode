class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            makeUp = target - nums[i]
            if makeUp in hashmap:
                return [hashmap[makeUp], i]
            hashmap[nums[i]] = i
        return []


solution = Solution()
print(solution.twoSum([3,3], 6))