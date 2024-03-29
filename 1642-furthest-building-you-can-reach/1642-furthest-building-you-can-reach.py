class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        index = []
        
        for i in range(len(heights) - 1):
            if heights[i + 1] - heights[i] > 0:
                temp = heights[i + 1] - heights[i]
                if temp > 0:
                    heapq.heappush(heap, temp)
                    
                if len(heap ) > ladders:
                    bricks -= heapq.heappop(heap)
                    
                if bricks < 0:
                    return i
                
        return len(heights) - 1
        
        