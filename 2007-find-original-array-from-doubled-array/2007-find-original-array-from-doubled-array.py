class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        heap, ans = [], []
        for x in changed:
            if heap and x==heap[0]*2:
                ans.append(heapq.heappop(heap))
            else:
                heapq.heappush(heap, x) 
        return ans if not heap else []