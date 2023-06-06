class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        pos = [0,0]
        for position in position:
            pos[position & 1] += 1
        return min(pos)