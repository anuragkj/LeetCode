class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        res = []
        stack = [0]
        next_high = [-1] * n
        for i in range(1, n):
            while stack and heights[stack[-1]] < heights[i]:
                curr = stack.pop()
                next_high[curr] = i
            stack.append(i)
        for i, j in queries:
            if i > j:
                i, j = j, i
            if i == j:
                res.append(i)
            elif heights[i] < heights[j]:
                res.append(j)
            elif next_high[i] == -1 or next_high[j] == -1:
                res.append(-1)
            else:
                curr = j
                while next_high[curr] != -1 and heights[curr] <= heights[i]:
                    curr = next_high[curr]
                if heights[curr] > heights[i]:
                    res.append(curr)
                else:
                    res.append(-1)
                    
        return res
