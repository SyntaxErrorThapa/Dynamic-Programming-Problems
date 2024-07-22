from functools import lru_cache
import json

class CoinChange:
    
    def brute_force_make_change(self, coins, amount):
        """_summary_
        Given a list of coin values, and an amount to be paid, 
        returns the shortest list of coins that add up to that amount.
        If the amount to be paid is zero, the empty list is returned.
        If the amount cannot be paid using coins, None is returned.
        """
        def helper(amount):
            # Handle payment of amount zero
            if amount == 0:
                return []
            
            # Negative amount cannot be paid 
            if amount < 0:
                return None 
            optimal_result = None # This is like the global value that keeps updating once the recursion is complete
            for coin in coins:
                # Solve a subproblem for the rest of the amount.
                remaining_amount = amount - coin
                partial_result = helper(remaining_amount) ## Think of it like a lock that locks the process from using the below code 
                # Skip this coin if payment is failed 
                if partial_result is None:
                    continue
                candidate = partial_result + [coin]
                # Check if the candidate solutionis better than the 
                # optimal solution know so far, and update it if needed.
                if (optimal_result is None or len(candidate) < len(optimal_result)):
                    optimal_result = candidate
            return optimal_result
        
        return helper(amount)
    
    
    def bottom_up_coin(self, coins, amount):
        """
        The whole logic is how can we move from bottom to up given recursive top-bottom
        We know at the bottom the value results to []
        The step above that we add the empty list with the coin
        This step gets iterative 
        """
        # Lets first initalize till amount because we want to find the no of coins that would require to reach the top which is amount
        result = [None] * (amount + 1)
        # Set the first value to [] as that is our base case
        result[0] = []
        
        # Move from 0 --> amount so that we can capture all the possible value 
        for possible_value in range(0, amount):
            if result[possible_value] is not None:
                # Move through all the items in the coin
                for coin in coins:
                    adding_coin = possible_value + coin
                    # We don't want our adding_coin to exceed the amount that is unnecessary
                    if adding_coin > amount:
                        continue
                    # Check the list for that amount index if none or have more len
                    if (result[adding_coin] is None or len(result[adding_coin]) > len(result[possible_value]) + 1):
                        result[adding_coin] = result[possible_value] + [coin]
        
        return result[amount]
    
    
    def bfs_coin(self, coins, amount):
        '''
        Optimized solution with less space complexity
        '''
        # Amount that cannot be paid are not stored
        # solutions[k] = optimal list of coins that add up to the amount k
        solution = {0: []}
        
        # List of amounts that can be paid but have not been handled yet
        queue = [0]
        while queue:
            value_in_queue = queue.pop(0)       
            intial_sol = solution[value_in_queue]
            
            
            if value_in_queue == amount:
                # Stop we found the first 
                # Due to BFS order, the first path reaching the required amount
                # is the one using the smalles t number of coins. Thus is the 
                # optimal solution
                print(solution)
                return solution[value_in_queue]

            for coin in coins:
                next_paid = coin + value_in_queue
                
                if next_paid > amount:
                    # Target amount is overpaid
                    continue
                if next_paid not in solution:
                    solution[next_paid] = intial_sol + [coin]
                    queue.append(next_paid)
                # All the element in solution can be paid with similar or better solution.
                # We can discard the amount
        # If not match found the coin does not exits and hence no combination of coins could match
        return None
        
    
    def top_down_count_pay(self, coins, value):
        
        memo = {}
        def helper(coins, amount):
            # Base case 
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            total_ways = 0
            for coin in coins:
                total_ways += helper(coins, amount - coin)
            memo[amount] = total_ways
            return total_ways
        total_ways = helper(coins, value)
        print(memo)
        return total_ways
                
    
    def top_down_count_pay_comb(self, coins, amount):
        # Dictionary to store the memoization results
        memo = {}

        def count_ways_helper(index, amount):
            # Check if the (index, amount) in memo
            if (index, amount) in memo:
                return memo[(index, amount)]
            
            # Check if the amount has reached 0
            if amount == 0:
                return 1
            
            # Invalid payment if we either pay too much or we still have something to pay but we ran out of coins
            if amount < 0 or index == len(coins):
                return 0
            
            total = 0
            coin = coins[index] # Kinda like local variable for each stack call
            for repeats in range(0, (amount // coin) + 1): # This includes not the coin -- all the coin included 0, 1, 2, 3 etc
                payment = repeats * coin # This would now 
                total = total + count_ways_helper(index + 1, amount - payment)
            memo[(index, amount)] = total
            return total    
        total_combo = count_ways_helper(0, amount);
        print(memo)
        return total_combo
     
coin = CoinChange()
# print(coin.brute_force_make_change([4,4,6], 8))
# print(coin.bottom_up_coin([4,4,6], 8))
# print(coin.bfs_coin([1, 2, 5], 9))
print(coin.top_down_count_pay([1, 2, 5], 5 ))
print(coin.top_down_count_pay_comb([1, 2, 5], 6))