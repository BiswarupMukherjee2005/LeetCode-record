class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if k not in nums:
            return k 
        i=1
        for i in range(len(nums)):
            c=(i+2)*k
            if (c%k==0) and c not in nums:
                return c