class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        s1=list(s)
        s2=list(t)
        s1.sort()
        s2.sort()
        if s1!=s2:
            return False
        return True