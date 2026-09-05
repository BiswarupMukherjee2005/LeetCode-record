class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        premax=[0]*n
        premin=[0]*n
        
        max=nums[0]
        for i in range(n):
            if nums[i]>max:
                max=nums[i]
            premax[i]=max
        min=nums[-1]
        for i in range(n-1,-1,-1):
            if nums[i]<min:
                min=nums[i]
            premin[i]=min
        
        for i in range(n):
            if (premax[i]-premin[i])<=k:
                return i
        return -1

