class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        num=''
        str_num=str(n)
        if n==0:
            return 0
        for i in str_num:
            if i!='0':
                num=num+i
                sum+=int(i)
        return int(num)*sum

        