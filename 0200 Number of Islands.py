# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # Check if an island
                # If island, increment count
                # Check for all surrounding islands
                # Turn each islands into a water
                if grid[row][col] == "1":
                    # print(f"found island at {row}, {col}")
                    islands += 1
                    self.cleanNeigboringIslands(grid, row, col)
        return islands
    
    def cleanNeigboringIslands(self, grid, row, col):
        if grid[row][col] == "0":
            return
        grid[row][col] = "0"
        if row > 0:
            self.cleanNeigboringIslands(grid, row - 1, col)
        if row < len(grid) - 1:
            self.cleanNeigboringIslands(grid, row + 1, col)
        if col > 0:
            self.cleanNeigboringIslands(grid, row, col - 1)
        if col < len(grid[0]) - 1:
            self.cleanNeigboringIslands(grid, row, col + 1)
            
