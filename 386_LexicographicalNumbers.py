from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        ans = []
        curr = 1
        for _ in range(n):
            ans.append(curr)

            if curr*10<=n:
                curr*=10
            else:
                while curr%10==9 or curr>=n :
                    curr//=10
                curr+=1
        
        return ans
        



'''
264

1   2 3 4 5 6 7 8 9
10  
100
101
..
109
11
110
111
...
119
12
120
13
14
15
16
17
18
19


'''