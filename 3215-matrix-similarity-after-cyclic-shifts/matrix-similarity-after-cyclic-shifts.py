class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        m = len(mat)       # Number of rows
        n = len(mat[0])    # Number of columns
        
        # We only care about k % n because shifting by the 
        # width of the row results in the same row.
        shift = k % n
        
        # If there's no effective shift, it's always true.
        if shift == 0:
            return True
            
        for i in range(m):
            for j in range(n):
                # Check if the current element matches the element 
                # at the position it would shift to/from.
                # This works for both left and right shifts!
                if mat[i][j] != mat[i][(j + shift) % n]:
                    return False
                    
        return True