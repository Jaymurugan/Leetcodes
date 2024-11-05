class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPalin(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

