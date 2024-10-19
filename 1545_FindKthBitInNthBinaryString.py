class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']

        while len(s)< k:
            t = [ '0' if x=='1' else '1' for x in s[::-1]]
            s.append('1')
            s.extend(t)
        
        return s[k-1]
    
