class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ind=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                ind.append(i)
        return ind