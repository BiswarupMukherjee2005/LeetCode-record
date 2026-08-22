class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m=n
        sum=0
        product=1
        while n>0:
            b=n%10
            sum+=b
            product*=b
            n=n//10
        return True if (m%(sum+product)==0) else False