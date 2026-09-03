class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2=[0]*len(nums1) #all odd or even
        c_o,c_e=0,0
        min_odd=float('inf')
        for i in nums1:
            if i%2==0:
                c_e+=1
            else:
                c_o+=1
                if min_odd>i:
                    min_odd=i
        if c_o==len(nums1) or c_e==len(nums1):
            return True
        for i in range(len(nums1)):
            if nums1[i]%2==1:
                nums2[i]=nums1[i]
            elif nums1[i]-min_odd>=1:
                nums2[i]=nums1[i]-min_odd
        if 0 in nums2:
            return False
        else:
            return True
    

