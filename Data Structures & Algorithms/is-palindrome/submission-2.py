import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        s1=re.sub(r'[^a-zA-Z0-9]', '', s1)
        for i in range(len(s1)):
            if s1[i]!=s1[(len(s1)-i-1)]:
                print((s1[i],s1[len(s1)-1-i]))
                return False
        return True