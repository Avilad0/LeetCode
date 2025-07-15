class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        
        hasVowel, hasConsonant = False, False
        vowels = "aeiou"

        for c in word:
            if c.isalpha():
                if c.lower() in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True
            elif not c.isdigit():
                return False
        
        return hasVowel and hasConsonant