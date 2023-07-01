# class Solution:
#     def backtrack(self, i: int, min_unfairness: int, distribution: List[int], cookies: List[int], k:int) -> int:
#         if i == len(cookies):
#             return min(min_unfairness, max(distribution))

#         if min_unfairness <= max(distribution):
#             return float('inf')
        
#         for j in range(k):
#             distribution[j] += cookies[i]
#             min_unfairness = min(min_unfairness, self.backtrack(i+1, min_unfairness, distribution, cookies, k))
#             distribution[j] -= cookies[i]

#         return min_unfairness

#     def distributeCookies(self, cookies: List[int], k: int) -> int:
#         return self.backtrack(0, float('inf'), [0] * k, cookies, k)
#The above soln gives TLE

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        distribution = [0] * k
        
        def backtrack(i):
            nonlocal min_unfairness, distribution
            
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return
            
            # Bounding condition to stop a branch if unfairness already exceeds current optimal solution
            if min_unfairness <= max(distribution):
                return
            
            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]
        
        backtrack(0)
        return min_unfairness