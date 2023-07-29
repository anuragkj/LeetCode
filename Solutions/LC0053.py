class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n%2 ==0: #Check if even or odd series is better, force the opponent to choose other
            return True
        memo = collections.defaultdict(int)
        
        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)
            
            memo[(left, right)] = max(score_by_left, score_by_right)
            return memo[(left, right)]
        
        return maxDiff(0, n - 1) >= 0