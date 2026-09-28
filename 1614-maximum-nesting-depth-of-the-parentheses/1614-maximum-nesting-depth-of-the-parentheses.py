class Solution:
    def maxDepth(self, s: str) -> int:
        max=0
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            if i==')':
                stack.pop()
            if len(stack)>max:
                max=len(stack)
        return max
        