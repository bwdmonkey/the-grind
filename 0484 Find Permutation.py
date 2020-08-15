# https://leetcode.com/problems/find-permutation/
# Leetcode August 2020 Week 3 Questions

# Version 1
class SolutionOne:
    def findPermutation(self, s: str) -> List[int]:
        # Keep track of result in reverse and stack of the secret signature
        reverse, stk = [], list(s)
        # Generate 1 ~ n + 1 options
        options = list(range(1, len(s) + 2))
        
        while stk:
            c = stk.pop()
            if c == "I":
                # If increasing, add the biggest option since its the last increase
                reverse += options.pop(),
            else:
                count = 1
                # Find all sequential decreases
                while stk and stk[-1] == "D":
                    stk.pop()
                    count += 1
                # Append the subarray of decreasing options to reverse
                idx = len(options) - count - 1
                for i in range(count):
                    reverse += options.pop(idx),
        # Append the one last remaining option
        reverse += options.pop(),
        
        # Reverse the results to get the correct answer
        return reversed(reverse)
       
# Version Two
class SolutionTwo:
    def findPermutation(self, s: str) -> List[int]:
        res, stk = [], []
        for i, c in enumerate(s):
            stk.append(i + 1)
            if c == "I":
                while len(stk):
                    res.append(stk.pop())
        stk.append(len(s) + 1)
        
        while stk:
            res.append(stk.pop())

        return res
                    
