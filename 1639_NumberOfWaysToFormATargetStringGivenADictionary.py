from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:


# TLE after 49/90 tests
# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         freq = []
#         i = 0
#         is_len_available = True
#         while is_len_available:
#             is_len_available = False
#             freq.append([0]*26)
#             for word in words:
#                 if len(word)>i:
#                     freq[i][ord(word[i])-97]+=1
#                     is_len_available = True
#             i+=1

#         total_ways = 0
#         max_word_len= len(freq)
#         target_len = len(target)
#         def dfs(min_word_index: int, target_index: int, ways: int):
#             if target_len == target_index:
#                 nonlocal total_ways
#                 total_ways+=ways
#                 return
            
#             target_char_to_int = ord(target[target_index])-97
#             for i in range(min_word_index, max_word_len):
#                 if freq[i][target_char_to_int]:
#                     dfs(i+1, target_index+1, ways*freq[i][target_char_to_int])
        
#         dfs(0, 0, 1)
#         return total_ways%1000000007