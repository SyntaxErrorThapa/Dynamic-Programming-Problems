class Frequent:
    def k_frequent(self, nums, k):
        # Sort as we add 
        # Sort as we add 
        dic_count = {}
        current_max = {}

        for i in nums:
            if i not in dic_count:
                dic_count[i] = 1
            else:
                dic_count[i] += 1
        
        bucket_sort = [None] * len(nums)
        print(dic_count)
        print(bucket_sort)
        for key, value in dic_count.items():
            if bucket_sort[value] is None:
                bucket_sort[value] = [key]
            else:
                bucket_sort[value].append(key)
        
        print(bucket_sort)
    
    def three_sum(self, nums):
        if len(nums) == 0:
            return []

        # Sort the array 
        nums.sort()
        result = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1 
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return result
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def notEmpty(length):
            return length != 0

        def check_int(num):
            try:
                int(num)
                return True
            except ValueError:
                return False
            
        stack = []

        for val in tokens:

            if check_int(val):
                stack.append(int(val))
            elif val == '+':
                if notEmpty(len(stack)):
                    first = stack.pop()
                    second = stack.pop()
                    result = second + first
                    stack.append(result)
            elif val == '*':
                if notEmpty(len(stack)):
                    first = stack.pop()
                    second = stack.pop()
                    result = second * first
                    stack.append(result)
            elif val == "/":
                if notEmpty(len(stack)):
                    first = stack.pop()
                    second = stack.pop()
                    result = int(second / first)
                    stack.append(result)
            elif val == "-":
                if notEmpty(len(stack)):
                    first = stack.pop()
                    second = stack.pop()
                    result = second - first
                    stack.append(result)
        
        return stack[0] if len(stack) == 1 else 0
    
    
f = Frequent()
print(f.k_frequent([1,1,1,2,2,3], 2))
print(f.three_sum([-1, 0, 1, 2, -1, -4]))
print(f.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
