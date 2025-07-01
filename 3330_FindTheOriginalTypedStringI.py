class Solution:
    def possibleStringCount(self, word: str) -> int:
        possible = 1

        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                possible+=1
        
        return possible