class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        arrows = ((b > a) - (b < a) for a, b in pairwise(nums))  # 1 up, -1 down, 0 flat
        return 1 + max((len(list(streak)) for arrow, streak in groupby(arrows) if arrow), default=0)