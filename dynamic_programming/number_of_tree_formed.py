class BST:
    
    def count_bsts(self, items):
        
        def helper(num_items):
            if num_items <= 1:
                return 1
            result = 0
            for num_items_left in range(num_items):
                num_bsts_left = helper(num_items_left)
                num_items_right = num_items -1 - num_items_left
                num_bsts_right = helper(num_items_right)
                result += num_bsts_left * num_bsts_right
    
            return result
        return helper(len(items))
    
b = BST()
print(b.count_bsts([1,2,3]))