class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt=0
        for i in arr1:
            temp=0
            for j in arr2:
                if abs(i-j)>d:
                    temp+=1
            if temp==len(arr2):
                cnt+=1
        return cnt
        

