from typing import List,Deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        l = len(deck)
        ans = [0]*l
        index = Deque(range(l))
        
        for c in deck:
            i = index.popleft()
            ans[i] = c
            if index:
                index.append(index.popleft())

        return ans
    
print(Solution().deckRevealedIncreasing([17,13,11,2,3,5,7]))


# Input: deck = [17,13,11,2,3,5,7]
#         [2,3,5,7,17,13,11]

#          0, 5,1, 6,2, 4,3 
# Output: [2,13,3,11,5,17,7]
# 
#
#
#input = [0,1,2,3,4,5,6,7,8,9,10,11]
#        [0,a,1,b,2,c,3, d,4,e,5, f]
#output= [0,6,1,9,2,7,3,11,4,8,5,10]
#
# a=6,b=9,c=7,d=11,e=8,f=10
#[1,b,2,c,3,d,4,e,5,f,a]
#[2,c,3,d,4,e,5,f,a,b]
#[3,d,4,e,5,f,a,b,c]
#[4,e,5,f,a,b,c,d]
#[5,f,a,b,c,d,e]
#[c,d,e,f,b]
#[e,f,b,d]
#[b,d,f]
#[f,d]
#[d]
