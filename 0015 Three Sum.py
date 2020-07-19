# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res, n = [], len(nums)
        for i in range(n):
            l, r = i + 1, n - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            while l < r:
                if r < n - 1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return res
