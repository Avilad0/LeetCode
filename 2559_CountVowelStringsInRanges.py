from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        allowed = set(['a','e','i','o','u'])
        prefixSum = [0]        
        for i in range(len(words)):
            prefixSum.append( prefixSum[i] + (1 if ((words[i][0] in allowed) and (words[i][-1] in allowed)) else 0))
        
        ans = []
        for l,r in queries:
            ans.append(prefixSum[r+1] - prefixSum[l])
        
        return ans

# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
#         allowed = set(['a','e','i','o','u'])
#         prefixSum = []        
#         prefixSum.append(1 if ((words[0][0] in allowed) and (words[0][-1] in allowed)) else 0)
        
#         for i in range(1, len(words)):
#             prefixSum.append( prefixSum[i-1] + (1 if ((words[i][0] in allowed) and (words[i][-1] in allowed)) else 0))
        
#         ans = []
#         for l,r in queries:
#             ans.append(prefixSum[r] - prefixSum[l] + (prefixSum[l] if l==0 else prefixSum[l]-prefixSum[l-1]))
        
#         return ans
    
print(Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])) # Output: [2,3,0]
print(Solution().vowelStrings( words = ["kzizbfceyysfjbkckouoqyrnxiobp","tfqjcavpwpyjmclwzjtyfpybipmynlkw","lrztxdla","gdhqqtobnaxvqgdzco","gcbzd","nuj","vferffslesxzofmidouariwuicauehfowcnv","czzeglsa","q","bzizqhugxngbkhfyxn","slebsmaccedlxjknmglsyexnfduue","oewsysetdvrtnuuws","su","benfnmdcavczz","lhkiksxegfbwnbllutdqnadrjz","qgauywpihdvysiwpkkxhvoglgedptnxvq","ghxnufgrapwzyvfxqxrpgr","ax","vivkmjjpust","p","jfxfeerpnpywxbxaqy","ciqqvebziztmmxhqltxnoklrpkdryupce","hsrlhcjvuapzyxkumaqdsqtffxxbudt"], 
                              queries = [[13, 19],[17, 17],[14, 22],[4, 21],[4, 10],[18, 19],[2, 20],[15, 19],[8, 12],[6, 18],[21, 21],[20, 20],[16, 22],[2, 2],[20, 21],[4, 8],[16, 17],[3, 13],[0, 10],[4, 14]])) 
                                # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])