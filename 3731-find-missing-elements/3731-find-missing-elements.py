class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn=min(nums)
        mx=max(nums)
        miss=[]
        for i in range(mn,mx+1):
            if i not in nums:
                miss.append(i)
        return miss