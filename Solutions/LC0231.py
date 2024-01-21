class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def f(n):
            if n<=2: return n
            return f(n-1)+f(n-2)
        return f(n)
        
