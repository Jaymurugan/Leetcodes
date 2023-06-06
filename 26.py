class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        last = 1
        while first<=last and last<len(nums):
            if nums[first] == nums[last]:
                last = last + 1
            else:
                nums[first+1] = nums[last]
                first = first +1
        return first + 1
