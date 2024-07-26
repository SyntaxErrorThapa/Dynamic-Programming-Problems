class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
            # Transpose
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
                            
        # Reverse each row 
        for i in range(len(matrix)):
            matrix[i].reverse()
                     
        print(matrix)

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])