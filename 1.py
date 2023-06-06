class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in x:
                return [x[diff], i]
            x[n]= i