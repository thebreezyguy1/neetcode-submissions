class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        def dfs(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True
            return False

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
            visited = set()
            if dfs(e1, e2):
                return [e1, e2]
        
        res = []

        
           
        return res