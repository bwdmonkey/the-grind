# https://leetcode.com/problems/closest-binary-search-tree-value/
# Leetcode August 2020 Week 2 Questions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # Idea: Recurse downward to see if any closest
        if root.val > target:
            if root.left:
                sub = self.closestValue(root.left, target)
                return self.closestToTarget(target, root.val, sub)
        elif root.val < target:
            if root.right:
                sub = self.closestValue(root.right, target)
                return self.closestToTarget(target, root.val, sub)
        
        return root.val
    

    def closestToTarget(self, target, val1, val2):
        return val1 if abs(target - val1) <= abs(target - val2) else val2
        
        
