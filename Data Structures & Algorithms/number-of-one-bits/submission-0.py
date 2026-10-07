class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=""
        while n>0:
            rem=n%2
            n//=2
            r=str(rem)+r
        c=0
        for i in r:
            if int(i)==1:
                c+=1
        return c
        