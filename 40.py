class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr = [], []

        def dfs(i):
            if sum(curr) == target:
                res.append(curr.copy())
                return

            if sum(curr) > target:
                return

            prev = -1

            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue

                curr.append(candidates[j])
                dfs(j + 1)
                curr.pop()
                prev = candidates[j]

        dfs(0)
        return res