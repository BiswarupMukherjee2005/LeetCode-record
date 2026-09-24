class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumnum(x):
            s=0
            while x>0:
                s+=x%10
                x=x//10
            return s
        for i in range(len(nums)):
            if i==sumnum(nums[i]):
                return i
        return -1
