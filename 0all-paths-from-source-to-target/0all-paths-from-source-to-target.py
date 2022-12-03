class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        edges = {}
        ans = []
        
        for i in range(len(graph)):
            for x in graph[i]:
                if i not in  edges:
                    edges[i] = []
                edges[i].append(x)
        
        stack = [0]
        def paths():
            node = stack[-1]
            if node == len(graph) - 1:
                return True
            
            for x in edges.get(node, []):
                stack.append(x)
                if paths(): 
                    ans.append(stack[:])
                    stack.pop()

            stack.pop()
            
        
        paths()
        return ans