# tc = O(m*n), sc=O(m*n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"

        m, n = len(num1), len(num2)
        num1, num2= num1[::-1], num2[::-1]

        ans = [0]*(m+n)
        for i in range(m):
            for j in range(n):
                prod = int(num1[i])*int(num2[j])
                ans[i+j] += prod
                ans[i+j+1] += (ans[i+j]//10)
                ans[i+j] = ans[i+j]%10

        while ans[-1]==0:
            ans.pop()

        return "".join(map(str, ans[::-1]))