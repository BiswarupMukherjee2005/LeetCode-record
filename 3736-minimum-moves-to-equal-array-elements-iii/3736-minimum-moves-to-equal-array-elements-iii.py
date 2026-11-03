class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=max(nums)
        cnt=0
        for i in nums:
            cnt+=(n-i)
        return cnt
        