#TLE Solution
# class Solution:
#     def dfs(self, curr_ind, prev_ind, arr, diff, dp):
#         if curr_ind == len(arr) - 1:
#             if len(arr) == 1:
#                 return 1
#             if arr[curr_ind] - arr[prev_ind] == diff:
#                 return 1
#             else:
#                 return 0

#         if dp[curr_ind][prev_ind] != -1:
#             return dp[curr_ind][prev_ind]
#         l2 = -float('inf')
#         l1 = 0 + self.dfs(curr_ind + 1, prev_ind, arr, diff, dp)
#         if (arr[curr_ind] - arr[prev_ind] == diff) or prev_ind == -1:
#             l2 = 1 + self.dfs(curr_ind + 1, curr_ind, arr, diff, dp)
#         dp[curr_ind][prev_ind] = max(l1, l2)
#         return dp[curr_ind][prev_ind]
        
#     def longestSubsequence(self, arr: List[int], difference: int) -> int:
#         dp = [[-1] * (len(arr)+1)]*(len(arr))
#         return self.dfs(0, -1, arr, difference, dp)

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        answer = 1
        for a in arr:
            before_a = dp.get(a - difference, 0)
            dp[a] = before_a + 1
            answer = max(answer, dp[a])
            
        return answer