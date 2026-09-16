class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        queue = deque([(0, -1)])
        visited = set([0])
        count = 0

        while queue:
            node, parent = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                queue.append((neighbor, node))
                visited.add((neighbor, node))
           
        return count == n
