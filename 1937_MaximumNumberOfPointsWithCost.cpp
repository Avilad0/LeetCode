#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxPoints(vector<vector<int>>& points) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);


        int m=points.size(), n=points[0].size(), i,j,k;
        vector<vector<long long>> dp(m, vector<long long>(n));
        for (i = 0; i < m; ++i) {
            std::copy(points[i].begin(), points[i].end(), dp[i].begin());
        }

        long long currMax;

        for(i=0;i<m;++i){
            currMax = INT_MIN;
            for(j=0;j<n;++j){
                if (i==0) dp[i][j]=max(dp[i][j], currMax); 
                else dp[i][j]=max(dp[i][j]+dp[i-1][j], currMax);
                
                currMax = dp[i][j]-1;
            }

            for(j=n-2;j>=0;--j){
                dp[i][j] = max(dp[i][j], dp[i][j+1]-1);
            }

        }

        return *max_element(dp[m-1].begin(), dp[m-1].end());
    }
};

// k=1;
// while (k<=j && points[i][j-k]< currMax-k) points[i][j-1]=currMax - k--;

int main(){
    Solution s;
    // vector<vector<int>> points = {{1,2,3},{1,5,1},{3,1,1}}; //9
    // vector<vector<int>> points = {{1,5},{2,3},{4,2}}; //11
    vector<vector<int>> points = {{ 8, 2, 4, 4, 9, 3, 5, 3,10,10},
 { 4, 8, 7, 4, 0, 1,10, 6, 4, 0},
 { 0, 5, 2,10, 4, 2, 7, 8, 6, 8},
 { 0, 1, 1, 2, 8, 0, 5, 9, 8, 2},
 { 6, 2, 0, 4, 5, 0, 5, 3,10, 3}}; //43
    
    cout<<s.maxPoints(points);
    return 0;
}

/*
ans:43

points:
[[ 8, 2, 4, 4, 9, 3, 5, 3,10,10],
 [ 4, 8, 7, 4, 0, 1,10, 6, 4, 0],
 [ 0, 5, 2,10, 4, 2, 7, 8, 6, 8],
 [ 0, 1, 1, 2, 8, 0, 5, 9, 8, 2],
 [ 6, 2, 0, 4, 5, 0, 5, 3,10, 3]]

dp:
[[ 8, 7, 7, 8, 9, 8, 8, 9,10,10],
 [14,15,14,15,16,17,18,17,16,15],
 [14,20,19,25,24,23,25,25,24,23],
 [14,21,20,27,32,31,30,34,33,32],
 [20,23,22,31,37,36,35,37,43,42]]
*/



/*

points = [[1,2,3],
          [1,5,1],
          [3,1,1]]

dp1    = [[1,2,3],
          [6,7,6],
          [9,8,7]]

dp0    = [[1,2,3],
          [2,7,4],
          [9,8,7]]

points = [[1,5],
          [2,3],
          [4,2]]
        
dp1     = [[4,5],
          [7,8],
          [11,10]]
        
dp0    = [[1, 5],
          [6, 8],
          [11,10]]

*/