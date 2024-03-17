class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        r=len(mat[0])-1
        l=0
        for i in range(len(mat)):
            if l==r:
                summ+= mat[i][l]
                l+=1
                r-=1
                
                
            else:
                summ+= mat[i][l]+mat[i][r]
                r-=1
                l+=1
        return summ  
            
     
            
        