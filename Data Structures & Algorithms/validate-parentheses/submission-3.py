class Solution:
    def isValid(self, s: str) -> bool:
        stack=''
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack=s[i]+stack
                continue
            elif s[i]==')':
                if len(stack)==0:
                    return False
                elif stack[0]!='(':
                    return False
                else:
                    stack=stack[1:]
                continue
            elif s[i]=='}':
                if len(stack)==0:
                    return False
                if stack[0]!='{':
                    return False
                else:
                    stack=stack[1:]
                continue
            elif s[i]==']':
                if len(stack)==0:
                    return False
                if stack[0]!='[':
                    return False
                else:
                    stack=stack[1:]
                continue
        if len(stack)>0:
            return False
        return True
                