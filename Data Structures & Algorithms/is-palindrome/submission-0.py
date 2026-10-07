class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        for i in s:
            if i.isalnum():
                r+=i.lower()
        
        start=0
        end=len(r)-1
        while(start<=end):
            if r[start] != r[end]:
                return False
            start+=1
            end-=1
        return True
        