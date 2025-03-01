#include<bits/stdc++.h>
using namespace std;

// bottom-up dp - space optimized
class Solution {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        int n = cost.size(), i, remain, withPay, withFree;
        vector<int> curr(n+1,0), next(n+1,1e9);
        next[0]=0;

        for (i=n-1; i>=0; i--){
            for (remain = 1; remain<=n; ++remain){
                withPay = cost[i] + next[max(0,remain-1-time[i])];
                withFree = next[remain];
                curr[remain] = min(withPay, withFree);
            }
            next = curr;
        }

        return curr[n];
    }
};

// // bottom-up dp 
// class Solution {
// public:
//     int paintWalls(vector<int>& cost, vector<int>& time) {
//         int n = cost.size(), i, remain, withPay, withFree;
//         vector<vector<int>> dp(n+1,vector<int>(n+1,0));

//         for (remain=1; remain<=n; ++remain) dp[n][remain] = 1e9;

//         for (i=n-1; i>=0; i--){
//             for (remain = 1; remain<=n; ++remain){
//                 withPay = cost[i] + dp[i+1][max(0,remain-1-time[i])];
//                 withFree = dp[i+1][remain];
//                 dp[i][remain] = min(withPay, withFree);
//             }
//         }

//         return dp[0][n];
//     }
// };

// // top-down dp ~ memoization
// class Solution {
// private:
//     int n;
//     vector<vector<int>> memo;
//     int dp(vector<int>& cost, vector<int>& time, int index, int remain){
//         if (remain<=0)  return 0;

//         if (index==n)   return 1e9;

//         if (memo[index][remain]!=-1)    return memo[index][remain];

//         int withPaid = cost[index] + dp(cost, time, index+1, remain - time[index] -1);
//         int withoutPaid = dp(cost, time, index+1, remain);

//         memo[index][remain] = min(withPaid, withoutPaid);
//         return memo[index][remain];
//     }
// public:
//     int paintWalls(vector<int>& cost, vector<int>& time) {
//         n=cost.size();
//         memo.resize(n,vector<int>(n+1,-1));
//         return dp(cost, time, 0, n);
//     }
// };


int main() {
    Solution s;
    vector<int> cost = {1,2,3,2};
    vector<int> time = {1,2,3,2};
    cout<<s.paintWalls(cost, time); //3
    // vector<int> cost = {2,3,4,2};
    // vector<int> time = {1,1,1,1};
    // cout<<s.paintWalls(cost, time); //4
    return 0;
}


/*
cost =[42,8,28,35,21,13,21,35], time = [2,1,1,1,2,1,1,2], output= 63
*/