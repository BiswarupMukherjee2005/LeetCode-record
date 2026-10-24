class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum_s=0
        sum_d=0
        for i in nums:
            if i>=10:
                sum_d+=i
            else:
                sum_s+=i
        return True if (sum_s>sum_d or sum_s<sum_d) else False