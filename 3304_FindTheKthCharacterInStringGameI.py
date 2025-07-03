class Solution:
    def kthCharacter(self, k: int) -> str:
        additions = 0
        while k != 1: 
            # let k = 2**t + x.  if x==0,  then prevK (k depends On) = k - 2**(t-1), else prevK (k depends On) = k - 2**t = x
            t = k.bit_length() - 1  
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            additions += 1

        return chr(ord("a") + additions)
    


# class Solution:
#     def kthCharacter(self, k: int) -> str:
#         arr = [0]
#         while len(arr)<k:
#             arr.extend([ (x+1)%26 for x in arr ])

#         return chr(97 + arr[k-1])