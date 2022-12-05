class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        bellman_ford = [float('inf')] * n
        bellman_ford[src] = 0
        
        for _ in range(k+1):
            bellman_ford_next = bellman_ford[:]
            for u, v, w in flights:
                bellman_ford_next[v] = min(bellman_ford_next[v], bellman_ford[u] + w)
            if bellman_ford_next == bellman_ford:
                break
            bellman_ford = bellman_ford_next
        
        return bellman_ford[dst] if bellman_ford[dst] != float('inf') else -1