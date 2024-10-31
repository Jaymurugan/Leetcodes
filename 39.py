class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curSet, res = [], []
        self.helper(0, curSet, res, target, candidates)
        return res

    def helper(self, i, curSet, res, target, candidates):
        if i >= len(candidates) or sum(curSet) > target:
            return

        if sum(curSet) == target:
            res.append(curSet.copy())
            return

        curSet.append(candidates[i])
        self.helper(i, curSet, res, target, candidates)
        curSet.pop()

        self.helper(i + 1, curSet, res, target, candidates)