class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        isZero = 0
        isNonZero = False
        for n in nums:
            if n == 0:
                isZero+=1
                continue
            isNonZero = True
            product*=n

        if not isNonZero:
            product = 0

        ans = []

        if isZero>1:
            ans = [0 for n in nums]
        elif isZero==1:
            for n in nums:
                if n==0:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
            ans = [ int(product/n) for n in nums]
        
        return ans