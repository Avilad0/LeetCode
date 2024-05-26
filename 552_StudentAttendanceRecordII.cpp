#include<bits/stdc++.h>
using namespace std;


class Solution {
private:
    int MOD = 1000000007;
    vector<vector<vector<int>>> memo;

    int checkCombinations(int n, int absenses, int consecutive_lates){
        if (absenses==2 || consecutive_lates==3){
            return 0;
        }
        if (n == 0){
            return 1;
        }

        if(memo[n][absenses][consecutive_lates]!=-1){
            return memo[n][absenses][consecutive_lates];
        }

        int combinations = checkCombinations(n-1, absenses, 0);
        combinations= (combinations + checkCombinations(n-1, absenses+1,0)) % MOD;
        combinations= (combinations + checkCombinations(n-1, absenses,consecutive_lates+1)) % MOD;

        return memo[n][absenses][consecutive_lates] = combinations;
    }

public:
    int checkRecord(int n) {
        memo = vector<vector<vector<int>>>(n + 1, vector<vector<int>>(2, vector<int>(3, -1)));
        return checkCombinations(n, 0, 0);
    }
};