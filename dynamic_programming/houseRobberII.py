class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(start, end):
            memo = {}
            
            def helper(index):
                if index in memo:
                    return memo[index]
                
                if index >= end:
                    return 0
                
                two_step = helper(index + 2) + nums[index]
                one_step = helper(index + 1)
                
                memo[index] = max(two_step, one_step)
                return memo[index]
            
            return helper(start)
        
        # Rob houses 0 to n-2 (excluding the last house)
        result1 = rob_line(0, len(nums) - 1)
        
        # Rob houses 1 to n-1 (excluding the first house)
        result2 = rob_line(1, len(nums))
        
        return max(result1, result2)

# Example usage:
solution = Solution()
test_cases = [
    [2, 3, 2],        # Expected output: 3
    [1, 2, 3, 1],     # Expected output: 4
    [1, 2, 3],        # Expected output: 3
    [0],              # Expected output: 0
    [4, 1, 2, 7, 5, 3, 1],  # Expected output: 14
]

for i, nums in enumerate(test_cases):
    print(f"Test case {i+1}: {nums} -> {solution.rob(nums)}")
