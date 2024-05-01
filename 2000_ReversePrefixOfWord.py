class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        i=0
        n=len(word)
        t = ""

        while i<n and word[i]!=ch:
            t = word[i] + t
            i+=1

        if i==n:
            return word
        else:
            return word[i] + t + word[i+1:]

        # i=0
        # n=len(word)
    
        # while i<n and word[i]!=ch:
        #     i+=1

        # if i==n:
        #     return word
        # else:
        #     return word[i::-1] + word[i+1:]


print(Solution().reversePrefix(word = "abcdefd", ch = "d")) #"dcbaefd"
print(Solution().reversePrefix(word = "xyxzxe", ch = "z")) #"zxyxxe"
print(Solution().reversePrefix(word = "abcd", ch = "z"))  #"abcd"
