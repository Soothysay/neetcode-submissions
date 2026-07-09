class Solution:
    def add(self,arr1):
        s={}
        arr=[arr1[i] for i in range(len(arr1))]
        for a in arr:
            if s.get(a)==None:
                s[a]=1
            else:
                s[a]+=1
        return s
    def isAnagram(self, s: str, t: str) -> bool:
        s1=self.add(s)
        t1=self.add(t)
        print(s1)
        print(t1)
        if s1==t1:
            return True
        return False
