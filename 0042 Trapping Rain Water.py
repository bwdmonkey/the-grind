# https://leetcode.com/problems/trapping-rain-water/

# Version One
class SolutionOne:
    def trap(self, A: List[int]) -> int:
        res, i, j = 0, 0, 0
        n = len(A)
        heights = []
        while j < n - 1:
            j += 1
            if A[i] > A[j]:
                for k in range(len(heights)):
                    if heights[k] < A[j]:
                        res += A[j] - heights[k]
                        heights[k] = A[j]
                heights.append(A[j])
            else:
                trap_height = min(A[i], A[j])
                res += sum([max(trap_height - h, 0) for h in heights])
                i, heights = j, []
        return res

# Version Two
class SolutionTwo:
    def trap(self, h: List[int]) -> int:
        count = 0
        l = 0
        r = len(h) - 1
        lmax = 0
        rmax = 0
        while l < r:
            if h[l] < h[r]:
                if h[l] > lmax:
                    lmax = h[l]
                else:
                    count += lmax - h[l]
                l += 1
            else:
                if h[r] > rmax:
                    rmax = h[r]
                else:
                    count += rmax - h[r]
                r -= 1
        return count
        
# Version Three
class SolutionThree:
    def trap(self, A: List[int]) -> int:
        if not A:
            return 0
        res, n = 0, len(A)
        lmaxs, rmaxs = [0] * n, [0] * n
        lmaxs[0], rmaxs[n - 1] = A[0], A[n - 1]
        
        for i in range(1, n, 1):
            lmaxs[i] = max(A[i], lmaxs[i - 1])
        for i in range(n - 2, -1, -1):
            rmaxs[i] = max(A[i], rmaxs[i + 1])
        for i, h in enumerate(A):
            res += min(lmaxs[i], rmaxs[i]) - h
            
        return res
