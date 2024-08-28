class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Const Variables
        row = len(grid)
        column = len(grid[0])
        count = 0

        def helper(r, c):
            # Condition to check before recursively changing the value 
            # Base Case
            if r >= 0 and r < row and c >= 0 and c < column and grid[r][c] == "1":
                # Mark as counted
                grid[r][c] = "0"
            
                # Recursively look 4 direction 
                helper(r-1, c)
                helper(r+1, c)
                helper(r, c-1)
                helper(r, c+1)
        
        # Initalization of the loop 
        for r in range(row):
            for c in range(column):
                if grid[r][c] == "1":
                    helper(r, c)
                    count += 1
        
        return count 

# Running the class 
num = Solution()
print(num.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))