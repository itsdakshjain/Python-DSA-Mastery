class Solution:
    
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        
        m = len(mat)       
        n = len(mat[0])    
        
        
        shift = k % n
        
        
        if shift == 0:
            
            return True
            
        for i in range(m):
            
            for j in range(n):
                
                if mat[i][j] != mat[i][(j + shift) % n]:
                    
                    return False
                    
        return True
