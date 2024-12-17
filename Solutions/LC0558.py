from functools import lru_cache

class Solution:  
    def countArrangement(self, n: int) -> int:  
        @lru_cache(None)
        def count_beautiful(pos, mask):
            if pos > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                if not (mask & (1 << num)) and (num % pos == 0 or pos % num == 0):
                    count += count_beautiful(pos + 1, mask | (1 << num))
            
            return count
        
        return count_beautiful(1, 0)
