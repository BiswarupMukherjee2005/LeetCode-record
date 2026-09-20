class Solution:
    def reverseDegree(self, s: str) -> int:
        x='abcdefghijklmnopqrstuvwxyz'
        v=26
        a={}
        for i in x:
            a[i]=v
            v-=1
        score=0
        for i in range(len(s)):
            score+=(i+1)*a[s[i]]
        return score 