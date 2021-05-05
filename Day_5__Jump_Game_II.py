#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

#Each element in the array represents your maximum jump length at that position.

#Your goal is to reach the last index in the minimum number of jumps.

#You can assume that you can always reach the last index.

 class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [float('inf') for _ in range(n)]
        arr[0] = 0
        
        for i in range(n):
            for j in range (1, nums[i]+1):
                if (i+j<n):
                    arr[i+j] = min(arr[i+j], arr[i]+1)
        return arr[-1]
