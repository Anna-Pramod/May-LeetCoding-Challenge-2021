#Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

#We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        mx = float('-inf')
        mn = float('inf')
        
        n=0
        m=0
        
        for i in range(len(nums)):
            if (mx>nums[i]):
                n = n + 1
            mx = max(mx,nums[i])
            
        for i in range((len(nums)-1), -1, -1):
            if (mn<nums[i]):
                m = m + 1
            mn = min(mn,nums[i])
            
        return (n<=1 or m<=1)
