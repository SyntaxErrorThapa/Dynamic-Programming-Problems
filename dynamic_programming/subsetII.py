class SubSet():
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        pal = []

        def helper(start):
            # Base Case
            if start == len(s):
                res.append(pal[:])
                return 
            
            # Recursive Case
            for i in range(start, len(s)):
                # Case if the item in palindrome
                if self.palindrome(s, start, i):
                    pal.append(s[ start : i+1 ])
                    helper(i + 1)
                    pal.pop()
        helper(0)
        return res

    def palindrome(self, s, i , j):
        while i < j:
            if s[i] != s[j]:
                return False 
            i += 1
            j -= 1
        return True
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        comb = []

        def helper(sums, start):
            # Base case 
            if sums > target:
                return 

            if sums == target: # Take a snapshot in the res
                res.append(comb[:])
                return 
            
            # Recursive Case
            for i in range(start, len(candidates)):
                # Case to check for duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                helper(sums+candidates[i], i + 1)
                comb.pop()
            
        helper(0, 0)
        return res

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to handle duplicates easily
        res = []
        sub = []

        def backtracking(start):
            res.append(sub[:])

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue

                sub.append(nums[i])
                backtracking(i + 1)
                sub.pop()

        backtracking(0)
        return res

# Example usage and test case
if __name__ == "__main__":
    subset_instance = SubSet()
    
    # Test Case 1
    nums1 = [1, 2, 2]
    result1 = subset_instance.subsetsWithDup(nums1)
    print(f"Test Case 1 - Input: {nums1}")
    print("Output:")
    print(result1)
    print()


    nums2 = [10,1,2,7,6,1,5]
    target = 8
    result2 = subset_instance.combinationSum2(nums2, target)
    print(f"Test Case 2 - Input: {nums2}")
    
    string = "aab"
    result = subset_instance.partition(string)
    print(result)