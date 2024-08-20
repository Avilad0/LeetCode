#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        memo =  vector<vector<int>> (piles.size(), vector<int>(piles.size()));
        
        suffixSum = piles;
        for (int i = suffixSum.size() - 2; i >= 0; --i)
            suffixSum[i] += suffixSum[i + 1];
        return maxStones(1, 0);
    }

private:

    vector<vector<int>> memo;
    vector<int> suffixSum;
    int maxStones(int maxTillNow, int currIndex) {
        if (currIndex + 2 * maxTillNow >= suffixSum.size()) return suffixSum[currIndex];
        if (memo[currIndex][maxTillNow] > 0) return memo[currIndex][maxTillNow];

        int res = INT_MAX;
        for (int i = 1; i <= 2 * maxTillNow; ++i) {
            res = min(res, maxStones(max(i, maxTillNow), currIndex + i));
        }
        memo[currIndex][maxTillNow] = suffixSum[currIndex] - res;
        return memo[currIndex][maxTillNow];
    }
};


/*
Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

m=1
    a) alice = [2,7] = 9
        m=2
            max for bob = [9,4,4] = 17
    
    b) alice = [2] = 2
        m=1
            max for bob = [7,9] = 16
            m=2
                alice = [4,4] = 8


Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104

m=1
    a) alice = [1] =1
        m=1
            max for bob = [2,3] = 5
            m=2
                alice = [4,5,100] = 109

    b) alice = [1] = 1
        m=1
            bob = [2] =2
            m=1
                alice = [3] =3
                m=1
                    bob = [4,5] = 9
                    m=2
                        alice = [100] =100
                        
*/