class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=""
        while n>0:
            rem=n%2
            n//=2
            r=str(rem)+r
        
        l=32-len(r)

        
        r="0"*l+r
        r=r[::-1]
        return int(r,2)

        