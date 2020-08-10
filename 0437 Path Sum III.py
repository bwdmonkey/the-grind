# https://leetcode.com/problems/path-sum-iii/
# Leetcode August 2020 Challenge Week 2 Questions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Version 1
class SolutionOne:
    def __init__(self):
        self.count = 0
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # Use helper function to simplify path calculations
        self.summedPaths(root, sum)
        return self.count
    
    def summedPaths(self, node: TreeNode, sum: int) -> List[int]:
        if node == None:
            return []
        paths = [0]
        # Append children paths - Ignore trivial case by the null check
        paths += self.summedPaths(node.left, sum)
        paths += self.summedPaths(node.right, sum)
        # Add node.val to all paths to get current level path sums
        paths = [i + node.val for i in paths]
        # Keep track of current level sum matches
        self.count += paths.count(sum)
        return paths
        

# Version 2
class SolutionTwo:
    def __init__(self):
        self.count = 0
        self.cursum = 0
        self.d = defaultdict(int)
    
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # If cursum == sum, increment count by default of 1
        self.d[0] = 1
        self.sum = sum
        self.pathSumHelper(root, 0)
        return self.count
        
    def pathSumHelper(self, node, cursum) -> None:
        if node == None:
            return
        
        cursum += node.val
        self.count += self.d[cursum - self.sum]
        
        # Add current sum for child node processing
        self.d[cursum] += 1
        self.pathSumHelper(node.left, cursum)
        self.pathSumHelper(node.right, cursum)
        # Remove current sum for same level subtree processing
        self.d[cursum] -= 1
