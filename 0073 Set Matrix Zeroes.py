# https://leetcode.com/problems/set-matrix-zeroes/

# Version One - O(mn) and O(m + n)
class SolutionOne:
    def setZeroes(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        n, m = len(M), len(M[0])
        
        for i in range(n):
            for j in range(m):
                if M[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    M[i][j] = 0
                    
# Version Two - O(mn) and O(1)
class SolutionTwo:
    def setZeroes(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        n, m = len(M), len(M[0])
        
        for i in range(n):
            if M[i][0] == 0:
                is_col = True
            for j in range(1, m):
                if M[i][j] == 0:
                    M[0][j] = 0
                    M[i][0] = 0
                    
        for i in range(1, n):
            for j in range(1, m):
                if M[0][j] == 0 or M[i][0] == 0:
                    M[i][j] = 0
        
        if M[0][0] == 0:
            for j in range(m):
                M[0][j] = 0
        
        if is_col:
            for i in range(n):
                M[i][0] = 0
