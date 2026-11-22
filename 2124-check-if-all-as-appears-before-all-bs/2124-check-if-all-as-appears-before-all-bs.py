class Solution:
    def checkString(self, s: str) -> bool:
        cnt_a=0
        cnt_b=0
        for i in s:
            if i=='a':
                cnt_a+=1
            else:
                cnt_b+=1
        cnt_before_b=0
        for i in s:
            if i=='b':
                break
            if i=='a':
                cnt_before_b+=1
        if cnt_a==cnt_before_b:
            return True
        else:
            return False