class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[]
        for i in range(n+1):
            temp =int(i)
            r=""
            c=0
            while temp>0:
                rem=temp%2
                temp//=2
                r=str(rem)+r
            for j in r:
                if int(j)==1:
                    c+=1
            l.append(c)
        return l


        