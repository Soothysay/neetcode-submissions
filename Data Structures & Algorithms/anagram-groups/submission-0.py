class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashana={}
        for s in strs:
            sor="".join(sorted(s))
            if sor in hashana:
                hashana[sor].append(s)
            else:
                hashana[sor]=[s]
        return list(hashana.values())