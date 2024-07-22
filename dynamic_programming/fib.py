import time

class Fib:

    # Give the last element in the fib
    def fib(self, index):
        
        first = 1
        second = 1
        for i in range(2, index):
            next = first + second
            first, second = second, next
        
        return second

    def down_top_fib(self, index):
        memo = [1, 1]
        # memo.append(1)
        # memo.append(1)
        for i in range(2, index):
            memo.append(memo[i-2] + memo[i-1])
        return memo[-1]
f = Fib()
start_time = time.time()
print(f.fib(5))
end_time = time.time()
print(f"fib method took {end_time - start_time:.10f} seconds")

# Measure time for the down_top_fib method
start_time = time.time()
print(f.down_top_fib(5))
end_time = time.time()
print(f"down_top_fib method took {end_time - start_time:.10f} seconds")

