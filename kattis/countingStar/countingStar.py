import sys

class CountingStar():
    def __init__(self, m, n):
        self.count = 0
        self.m = m
        self.n = n

    def traversal(self, grid, r, c):
        # Case to check if out of bound
        if r >= 0 and r < self.m and c >= 0 and c < self.n and grid[r][c] == "-":
            grid[r][c] = '#'
        
            # Recursively traverse all four directions
            self.traversal(grid, r - 1, c)
            self.traversal(grid, r + 1, c)
            self.traversal(grid, r, c - 1)
            self.traversal(grid, r, c + 1)

    def counting_star(self, grid):
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] == "-":
                    self.traversal(grid, r, c)
                    self.count += 1
        return self.count

def main():
    input = sys.stdin.read
    data = input().splitlines()

    # The first line contains two integers, m and n
    m, n = map(int, data[0].split())

    # The next m lines are the grid
    grid = [list(data[i+1]) for i in range(m)]

    # Create an instance of CountingStar and count the stars
    counter = CountingStar(m, n)
    result = counter.counting_star(grid)

    # Output the result
    print(result)

if __name__ == "__main__":
    main()
