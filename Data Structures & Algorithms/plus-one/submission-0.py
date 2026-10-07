class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        l=[]
        for i in digits:
            s+=str(i)
        s=int(s)
        s+=1
        s=str(s)
        for i in s:
            l.append(int(i))
        return l


        