class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        all_letters = set(s)
        count = 0
        for c in all_letters:
            left,right = s.index(c) , s.rindex(c)
            unique_letters_middle = set(s[left+1:right])
            count+=len(unique_letters_middle)
            
        return count