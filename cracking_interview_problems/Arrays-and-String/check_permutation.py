class CheckPermutation:
    
    def check_permutation(self, s1, s2):
        # S1 in hash table 
        dic = {}
        for i in s1:
            dic[i] = 1
        
        l = 0
        r = 0
        while r < len(s2):
            if s2[r] in dic:
                l = r
                for i in range(r, len(s1) + r):
                    if i < len(s2) and s2[i] not in dic:
                        return False
                return True
                        
            r+=1
