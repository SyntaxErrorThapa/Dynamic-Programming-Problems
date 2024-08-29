class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Const Variables
        row = len(grid)
        column = len(grid[0])
        self.max_area = 0

        def helper(r, c):
            # Base case when out of bound 
            if r < 0 or c < 0 or r >= row or c >=column or grid[r][c] == "0":
                return 0
            grid[r][c] = "0"
                
            # Recursive Case
            return 1 + helper(r + 1, c) + helper(r - 1, c) + helper(r, c + 1) + helper(r, c - 1)

        for r in range(row):
            for c in range(column):

                if grid[r][c] == "1": # We have an island 
                    self.max_area = max(helper(r, c), self.max_area)

        return self.max_area
    
# Running the class 
num = Solution()
print(num.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))