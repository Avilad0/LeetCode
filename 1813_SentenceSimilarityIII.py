class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        s1Words, s2Words = sentence1.split(" "), sentence2.split(" ")
        
        s1L,s1R = 0, len(s1Words)-1
        s2L,s2R = 0, len(s2Words)-1
        
        isChanged = True
        while isChanged and s1L<=s1R and s2L<=s2R:
            isChanged = False
            if s1Words[s1L] == s2Words[s2L]:
                s1L+=1
                s2L+=1
                isChanged = True
            
            if s1Words[s1R] == s2Words[s2R]:
                s1R-=1
                s2R-=1
                isChanged = True
        
        return s1L>s1R or s2L>s2R

print(Solution().areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))