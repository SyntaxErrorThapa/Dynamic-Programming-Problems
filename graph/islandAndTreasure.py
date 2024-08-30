from collections import deque
from typing import List 

class GridDebugger:
    def __init__(self, grid):
        self.grid = grid 
        
    def print_grid(self):
        for row in self.grid:
            print(row)
        print()
        
    def islandsAndTreasure(self):
        row = len(self.grid)
        column = len(self.grid[0])
        visited = set()
        q = deque()
        
        def helper(r, c):
            # Base case
            if r >= row or c >= column or r < 0 or c < 0 or self.grid[r][c] == -1 or (r, c) in visited:
                return 
            # Add the value to set and queue 
            visited.add((r, c))
            q.append([r, c])
        
        # Find all the 0 first 
        for r in range(row):
            for c in range(column):
                if self.grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))
                    
        dist = 0
        # Expand the path using BFS 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                self.grid[r][c] = dist
                
                helper(r + 1, c)
                helper(r - 1, c)
                helper(r, c + 1)
                helper(r, c - 1)
                
            dist += 1
        
# Example usage
input_grid = [
  [14,-1,0,14],
  [14,14,14,-1],
  [14,-1,14,-1],
  [0,-1,14,14]
]

debugger = GridDebugger(input_grid)
debugger.islandsAndTreasure()