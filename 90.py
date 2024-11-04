class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subSet, res = [], []
        self.helper(0, subSet, res, nums)
        return res

    def helper(self, i, subSet, res, nums):
        if i >= len(nums):
            res.append(subSet.copy())
            return

        subSet.append(nums[i])
        self.helper(i + 1, subSet, res, nums)
        subSet.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, subSet, res, nums)