class Solution:
    def isValid(self, s: str) -> bool:
        o={'{','[','('}
        d={'}':'{',
           ']':'[',
           ')':'('}
        st=[]

        for b in s:
            if b in o:
                st.append(b)
            else:
                if not st or d[b] != st[-1]:
                    return False
                st.pop()
        return len(st)==0
        