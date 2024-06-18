class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse=True)
        ans = 0
        heap = [(-p,d) for d,p in zip(difficulty,profit)]
        heapify(heap)

        for w in worker:
            while heap and heap[0][1]>w:
                heappop(heap)
            
            if not heap:
                break
            ans+=heap[0][0]

        return -ans
        
