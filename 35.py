class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)

        if target < nums[0]:
            return 0

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = int((start + end)/2)
            if nums[mid] > target:
                end = mid - 1
                if end >= 0:
                    if nums[end] < target:
                         return end + 1
                else:
                     return 0

            elif nums[mid] < target:
                start = mid + 1
                if start < len(nums):
                    if nums[start] > target:
                        return start
                else:
                    return len(nums)
            else:
                return mid