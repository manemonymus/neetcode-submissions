class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while (len(stones)>1):
            stones.sort()
            x=stones[-2]
            y=stones[-1]
            if x==y:
                stones=stones[:-2]
            else:
                stones=stones[:-2]
                stones.append(y-x)
        if len (stones)==0:
            return 0
        return stones[0]
        