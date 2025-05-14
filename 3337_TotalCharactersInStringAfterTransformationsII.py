from typing import List

MOD = 10**9 + 7
NUM_OF_CHARS = 26

class Matrix:
    def __init__(self, otherMatrix = None):
        self.arr = [[0]*NUM_OF_CHARS for _ in range(NUM_OF_CHARS)]
        if otherMatrix!=None:
            for i in range(NUM_OF_CHARS):
                for j in range(NUM_OF_CHARS):
                    self.arr[i][j] = otherMatrix.arr[i][j]

    def __mul__(self, otherMatrix):
        ans = Matrix()
        for i in range(NUM_OF_CHARS):
            for j in range(NUM_OF_CHARS):
                for k in range(NUM_OF_CHARS):            
                    ans.arr[i][j] = (ans.arr[i][j] + self.arr[i][k]*otherMatrix.arr[k][j])%MOD
        
        return ans
        

class Solution:
    def matrixExponentiation(self, transformMatrix: Matrix, t:int):
        ans = Matrix()
        for i in range(NUM_OF_CHARS):
            ans.arr[i][i]=1

        curr = Matrix(transformMatrix)
        while t>0:
            if t&1:
                ans = ans*curr
            curr = curr*curr
            t>>=1

        return ans

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        transformMatrix = Matrix()
        for i in range(NUM_OF_CHARS):
            for j in range(1, nums[i]+1):
                transformMatrix.arr[(i+j)%NUM_OF_CHARS][i]+=1
        
        exponentiatedMatrix: Matrix = self.matrixExponentiation(transformMatrix, t)

        freq = [0]*NUM_OF_CHARS
        for c in s:
            freq[ord(c)-97]+=1
        
        totalLength = 0
        for i in range(NUM_OF_CHARS):
            for j in range(NUM_OF_CHARS):
                totalLength=  (totalLength + exponentiatedMatrix.arr[i][j]*freq[j])%MOD

        return totalLength