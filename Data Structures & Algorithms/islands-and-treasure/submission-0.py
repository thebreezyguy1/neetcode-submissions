class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        num_rows, num_cols = len(grid), len(grid[0])
        def get_neighbors(coord):
            r, c = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = r + delta_row[i]
                neighbor_col = c + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    res.append((neighbor_row, neighbor_col))
            return res
        
        queue = deque()
        visited = set()
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        distance = 0
        while len(queue) > 0:
            n = len(queue)
            distance += 1
            for _ in range(n):
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if neighbor in visited:
                        continue
                    if grid[r][c] == INF:
                        grid[r][c] = distance
                        queue.append(neighbor)
                    visited.add(neighbor)
            