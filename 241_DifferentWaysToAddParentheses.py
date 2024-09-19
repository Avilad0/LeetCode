from typing import List

class Solution:
    
    memo = dict()

    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        if expression in self.memo:
            return self.memo[expression]
        
        if len(expression)==0:
            return []
        
        if len(expression)==1 or (len(expression)==2 and expression.isdigit()):
            return [int(expression)]
        
        results =[]
        for i, ch in enumerate(expression):

            if(ch.isdigit()):
                continue
             
            leftResults = self.diffWaysToCompute(expression[:i])
            rightResults = self.diffWaysToCompute(expression[i+1:])

            for left in leftResults:
                for right in rightResults:
                    if ch=='*':
                        results.append(left*right)
                    elif ch=='-':
                        results.append(left-right)
                    elif ch=='+':
                        results.append(left+right)
        
        self.memo[expression] = results
        return results





'''
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

2 -> *3 -> -4 ->  *5
        -> -4*5
     *3-4 -> *5
2*3 -> -4 -> *5
    -> -4*5
'''