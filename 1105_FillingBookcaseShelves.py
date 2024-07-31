from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = books[0][1]

        for i in range(2, n + 1):
            remainingWidth = shelfWidth - books[i - 1][0]
            maxHeight = books[i - 1][1]
            dp[i] = books[i - 1][1] + dp[i - 1]

            j = i - 1
            while j > 0 and remainingWidth - books[j - 1][0] >= 0:
                maxHeight = max(maxHeight, books[j - 1][1])
                remainingWidth -= books[j - 1][0]
                dp[i] = min(dp[i], maxHeight + dp[j - 1])
                j -= 1

        return dp[n]