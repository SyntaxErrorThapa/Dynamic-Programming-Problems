import sys

class PickUpStick:
    
    def __init__(self, m, n):
        self.m = m
        self.n = n
        
    def pick_up_stick(self):
        # 1st vertex 

def main():
    input = sys.stdin.read
    data = input().splitlines()

    # The first line contains two integers, m and n
    m, n = map(int, data[0].split())

    # The next m lines are the grid
    grid = [list(data[i+1]) for i in range(m)]

    # Create an instance of CountingStar and count the stars
    counter = PickUpStick(m, n)
    result = counter.counting_star(grid)

    # Output the result
    print(result)

if __name__ == "__main__":
    main()