# https://leetcode.com/problems/merge-k-sorted-lists/

from heapq import heappush, heappop

# Wrapper around ListNode to make it comparable
class Wrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Idea: Use heapsort
        q = []
        head = node = ListNode()
        
        # 1. Append nodes to heapq – Note: Possibly empty nodes
        for ln in lists:
            if ln:
                heappush(q, Wrapper(ln))
        
        # 2. Pop from heap, append to head, add next if any
        while q:
            node.next = heappop(q).node
            node = node.next
            if node.next:
                heappush(q, Wrapper(node.next))
        
        # 3. Drop placeholder value
        return head.next
