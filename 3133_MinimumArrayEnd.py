class Solution:
    def minEnd(self, n: int, x: int) -> int:
        mask,n = 1,n-1

        while n>0:
            if (x & mask)==0:
                x |= (mask * (n%2))
                n >>= 1

            mask <<= 1

        return x

'''
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i,j,n=0,1,n-1
        while j<=n:
            while (x & (1<<i))!=0:
                i+=1

            if (n//j)%2:
                x = x | (1<<i) 

            j*=2
            i+=1

        return x
'''
    
print(Solution().minEnd(6,1)) #30
# print(Solution().minEnd(15,4)) #30
# print(Solution().minEnd(4,4)) #7
# print(Solution().minEnd(3,4))
# print(Solution().minEnd(2,7))

'''
ans = 11, 1011
n = 6
x = 1
0001
0011
0101
0111
1001
1011  --
1101
1111

((5/4)%2) + ((5/2)%2) + ((5/1)%2) + 1  =  1011 = 11



Example 1:
Input: n = 3, x = 4
Output: 6

Explanation:
nums can be [4,5,6] and its last element is 6.

x = 100

  00100
  00101
  00110
  00111
  01100
  01101
  01110
  01111
  10100
  10101
  10110
  10111  
  11100
  11101
  11110
  11111

if n=15, output  - 11110 = 16+8+4+2 = 30

((ceil(n/8))%2==1: 0 else 1 ) ((ceil(n/4))%2==1: 0 else 1 ) 1 ( (ceil(n/2))%2==1: 0 else 1 ) ( if ceil(n/1)%2==1: 0 else 1 )
11110

or 
n=n-1
((n/8)%2) ((n/4)%2) 1 ((n/2)%2) ((n/1)%2)
((n/(1<<j)))
11110

Example 2:
Input: n = 2, x = 7
Output: 15

Explanation:
nums can be [7,15] and its last element is 15.
'''