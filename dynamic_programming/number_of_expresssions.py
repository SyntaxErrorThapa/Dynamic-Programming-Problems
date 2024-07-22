import time

class NumberOfExpression:
    def count_expression(self, numbers, target_result):
        memo={}
        def helper(index, numbers, target_result):
            # Base Case
            if index == len(numbers):
                if target_result == 0:
                    return 1
                return 0
            if (index,target_result) in memo:
                return memo[(index,target_result)]
            
            count = 0
            
            count = count + helper(index + 1, numbers, target_result + numbers[index])
            count = count + helper(index + 1, numbers, target_result - numbers[index])
            memo[(index,target_result)] = count
            return count
        
        value = helper(0, numbers, target_result)
        print(memo)
        return value
    

    def bottom_up_bfs_count_expression(self, numbers, target_result):
        
        # The structure is that Initially the numbers[0] has count 1
        initial_dic = {numbers[0] : 1}
        for index in range(1, len(numbers)):
            # Create new dic that replaces the old dic
            new_dic = {}
            for key, value in initial_dic.items():
                
                new_result_add = key + numbers[index]
                new_result_substract = key - numbers[index]
                
                # Check if they are in dic 
                if new_result_add in new_dic:
                    new_dic[new_result_add] += value
                else:
                    new_dic[new_result_add] = value
                
                if new_result_substract in new_dic:
                    new_dic[new_result_substract] += value
                else:
                    new_dic[new_result_substract] = value
            
            initial_dic = new_dic
        return initial_dic[target_result]
        
    
no = NumberOfExpression()
start = time.time()
print(no.count_expression([1,2,2,3,3], 7))
end = time.time()
print(f"{end - start: .10f}")
print(no.bottom_up_bfs_count_expression([1,2,2,3,3], 7))