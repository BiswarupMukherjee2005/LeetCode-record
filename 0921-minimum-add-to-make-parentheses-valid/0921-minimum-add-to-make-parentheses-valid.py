class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if len(stack)!=0:
                if stack[-1]=='(' and i ==')':
                    stack.pop()
                    continue
            
            stack.append(i)
        return len(stack)