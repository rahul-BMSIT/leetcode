class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        cur, pprev, prev = 1, 1, 2

        for _ in range(n - 2):
            cur = pprev + prev
            pprev, prev = prev, cur

        return cur