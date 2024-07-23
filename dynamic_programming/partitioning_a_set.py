class Partition:
    def top_down_equal_partition(self, numbers, target):
        
        memo = {}
        
        def helper(index, target):
            # Base case when we found the partition
            if target == 0:
                return True
            # Base case to help optimize the algorithm
            if (index, target) in memo:
                return memo[(index, target)]
            # Base case to avoid illegal transition
            if index >= len(numbers) or target < 0:
                return False
            
            no = numbers[index]
            
            # First we don't include the number
            include_result = helper(index + 1, target - no)
            
            # Then we include the number
            exclude_result = helper(index + 1, target)
            result = include_result or exclude_result
            
            memo[(index, target)] = result
            return result
        
        # Condition when it is considered false 
        if sum(numbers) % 2 == 1:
            return False

        half_sum = sum(numbers) // 2
        bool_form = helper(0, half_sum)
        print(memo)
        # Only needed to do the one half 
        return bool_form
    
par = Partition()
print(par.top_down_equal_partition([2,3,5,6], 8))