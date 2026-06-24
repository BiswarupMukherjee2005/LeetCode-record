class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for k in range(1,len(nums)):
            if nums[i]==nums[k]:
                continue
            else:
                i+=1
                nums[i]=nums[k]
        return i+1