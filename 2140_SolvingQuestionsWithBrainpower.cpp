#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();

        vector<long long> dp(n+1,0);
        
        for (int i=n-1; i>=0; --i){
            if (i+questions[i][1] + 1 < n){
                dp[i] = max(dp[i+1], questions[i][0] + dp[i+questions[i][1] + 1]);
            } else {
                dp[i] = max(dp[i+1], (long long) questions[i][0]);
            }
        }

        return dp[0];
    }
};

int main(){
    Solution s;
    vector<vector<int>> questions = {{21,5},{92,3},{74,2},{39,4},{58,2},{5,5},{49,4},{65,3}}; // output = 157
    cout<<s.mostPoints(questions);
    return 0;
}


/*
questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]], output = 157


*/