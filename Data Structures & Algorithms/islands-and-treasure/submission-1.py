class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        num_rows, num_cols = len(grid), len(grid[0])

        def bfs(queue):
            count = 0
            while queue:
                count += 1
                for _ in range(len(queue)):
                    node = queue.popleft()
                    row, col = node

                    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        neighbor_row, neighbor_col = row + x, col + y
                        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                            if (neighbor_row, neighbor_col) in visited or grid[neighbor_row][neighbor_col] in [-1, 0]:
                                continue
    
                            grid[neighbor_row][neighbor_col] = min(grid[neighbor_row][neighbor_col], count)
                            queue.append((neighbor_row, neighbor_col))
                            visited.add((neighbor_row, neighbor_col))
        
        queue = deque()
        visited = set()

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        bfs(queue)
