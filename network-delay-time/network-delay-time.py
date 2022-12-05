from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq
        nodes = []
        dist = [float('inf')] * (n + 1)
        ans = 0
        dist[k] = 0
        
        visited = set()
        visited.add(k)
        
        edges = [[] for _ in range(n + 1)]
        for u, v, w in times:
            edges[u].append((v, w))
        
        for v, w in edges[k]:
            heapq.heappush(nodes, (w, v))

        while nodes:
            if len(visited) == n:
                break
            w, u = heapq.heappop(nodes)
            if u in visited:
                continue
            visited.add(u)
            dist[u] = w
            for v, w in edges[u]:
                heapq.heappush(nodes, (w + dist[u], v))
        
        for i in range(1, n + 1):
            ans = max(ans, dist[i])
        
        return ans if ans != float('inf') else -1