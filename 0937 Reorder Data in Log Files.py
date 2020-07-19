# https://leetcode.com/problems/reorder-data-in-log-files/

from heapq import heappush, heappop

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterHeap = []
        digitResult = []
        
        for val in logs:
            head, tail = val.split(" ", 1)
            # doesn't work with "id a"
            # first, rest = tail.split(" ", 1)
            words = tail.split(" ", 1)
            if words[0].isdigit():
                digitResult.append(val)
            else:
                heappush(letterHeap, (tail, val))
                
        result = [heappop(letterHeap)[1] for i in range(len(letterHeap))]
        result += digitResult
        return result
        
        
        
                
                
            
