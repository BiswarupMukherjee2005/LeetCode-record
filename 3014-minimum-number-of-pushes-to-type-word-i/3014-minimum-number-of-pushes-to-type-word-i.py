class Solution:
    def minimumPushes(self, word: str) -> int:
        count=0
        k=0
        adder=1
        for i in word:
            if k==8:
                k=0
                adder+=1
            count+=adder
            k+=1
        return count