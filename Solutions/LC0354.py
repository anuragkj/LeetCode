class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            # If the combination is done
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                # Add nums[i] into the current combination
                curr.append(nums[i])

                # Use the next integers to complete the combination
                backtrack(i + 1, curr)

                # Backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output
