class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d={

        }
        for i in nums:
            d[i]=1+d.get(i,0)
        for i in d:
            if d[i]==1:
                return i