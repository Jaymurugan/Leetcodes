class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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

        self.helper(i + 1, subSet, res, nums)