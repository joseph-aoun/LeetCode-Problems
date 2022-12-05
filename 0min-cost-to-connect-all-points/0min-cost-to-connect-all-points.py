from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        visited = []
        for i in range(len(points)):
            visited.append(False)
        visited[0] = True
        heap = []
        for i in range(1, len(points)):
            heapq.heappush(heap, (abs(points[0][0] - points[i][0]) + abs(points[0][1] - points[i][1]), i))
        ans = 0
        while heap:
            cost, i = heapq.heappop(heap)
            if visited[i]:
                continue
            visited[i] = True
            ans += cost
            for j in range(len(points)):
                if visited[j]:
                    continue
                heapq.heappush(heap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))
        return ans