#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numWays(vector<string>& words, string target) {
        int m= words.size(), n=words[0].length(), tn = target.length();
        const int mod=1e9 + 7;

        vector<vector<int>> freq(n, vector<int>(26,0));

        for (int i=0;i<m;++i){
            for (int j=0;j<n;++j){
                freq[j][words[i][j]-'a']++;
            }
        }

        vector<vector<int>> dp(n+1, vector<int>(tn+1,0));
        for (int i=0;i<=n;++i)  dp[i][0]=1;

        for (int i=1; i<=n; ++i){
            for (int ti=1;ti<=tn;++ti){
                dp[i][ti] = (dp[i-1][ti] + ((long long)dp[i-1][ti-1] * freq[i-1][target[ti-1]-'a']))%mod;
            }
        }

        return dp[n][tn];
    }
};

// // top-down DP, memoization
// class Solution {
// private:
//     vector<vector<int>> freq, memo;
//     int m,n, tn, mod=1e9 + 7;
//     long long backtrack(int fIndex, string& target, int targetIndex){
//         if (targetIndex==tn)    return 1;
        
//         if (n-fIndex<tn-targetIndex)  return 0;

//         if (memo[targetIndex][fIndex]!=-1)  return memo[targetIndex][fIndex];
        
        
//         int curr = 0;
//         if (freq[fIndex][target[targetIndex]-'a']>0){
//             curr = (backtrack(fIndex+1, target, targetIndex+1) * freq[fIndex][target[targetIndex] - 'a'])%mod;
//         }
//         curr = (backtrack(fIndex+1, target, targetIndex) + curr)%mod;
//         return memo[targetIndex][fIndex] = curr;
//     }

// public:
//     int numWays(vector<string>& words, string target) {
//         m= words.size();
//         n=words[0].length();
//         tn = target.length();
//         freq.resize(n, vector<int>(26,0));
//         memo.resize(tn, vector<int>(n,-1));

//         for (int i=0;i<m;++i){
//             for (int j=0;j<n;++j){
//                 freq[j][words[i][j]-'a']++;
//             }
//         }

//         return (int) backtrack(0, target, 0);
//     }
// };

int main(){
    Solution s;
    // vector<string> words = {"abba","baab"};
    // string target = "bab";
    
    vector<string> words = {"daa","bcc","ddb","bbd"};
    string target = "ba";
    // ans = 5
    
    cout<<s.numWays(words, target);
    return 0;
}