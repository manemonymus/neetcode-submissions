class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative=False
        y=str(x)
        if y[0]=="-":
            negative = True
        
        
        if negative:
            
            y=y[1:]
            y=y[::-1]
            if int(y)*-1 <-2**31:
                return 0
            return int(y)*-1
        if int(y[::-1]) > (2**31)-1:
            return 0
        return int(y[::-1])
        
        