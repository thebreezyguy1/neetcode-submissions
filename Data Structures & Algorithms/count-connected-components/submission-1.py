class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        count = 0
        visited = set()

        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        for i in range(n):
            if i not in visited:
                print(i)
                visited.add(i)
                bfs(i)
                count += 1
        
        return count