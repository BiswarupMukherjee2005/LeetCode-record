class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if n==100:
            return 100
        else:
            for i in range(n,100+1):
                b=i%10
                a=i//10
                if (a==0):
                    a=1
                if (a*b)%t==0:
                    return n
                else :
                    n+=1
        