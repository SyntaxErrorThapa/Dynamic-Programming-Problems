class IsUnique:
    
    def isunique(self, word):
        '''
        No additional data structure allowed 
        '''
        unique = [False] * 128
        for i in word:
            ascii_val = ord(i)
            if unique[ascii_val]:
                return False
            unique[ascii_val] = True
            
        return True
    
    
    def using_bit_opertor(self, word):
        val = 0
        for i in word:
            ascii_val = ord(i)
            if val & (1 << ascii_val) > 0:
                return False
            
            val |= 1 << ascii_val
        return True
    
i = IsUnique()

print(i.isunique("abcddd"))
print(i.using_bit_opertor("abc"))