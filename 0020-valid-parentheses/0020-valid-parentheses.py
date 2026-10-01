class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s :
            if i in '([{':
                stack.append(i)
            else:
                if len(stack)!=0:
                    if stack[-1]=='(' and i==')':
                        stack.pop()
                    elif stack[-1]=='[' and i==']':
                        stack.pop()
                    elif stack[-1]=='{' and i=='}':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        return True if len(stack)==0 else False