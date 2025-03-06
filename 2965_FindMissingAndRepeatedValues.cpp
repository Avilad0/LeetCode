#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size(),n2=n*n,i, j;
        long long sumOfN = ((long long)n2*(n2+1))/2, sumOfN2 = ((long long)n2*(n2+1)*(2*n2 + 1))/6, runningSumOfN=0, runningSumOfN2=0;
        
        for (i=0; i<n; ++i){
            for (j=0; j<n; ++j){
                runningSumOfN += grid[i][j];
                runningSumOfN2 += (grid[i][j]*grid[i][j]);
            }
        }
        
        int xMy = runningSumOfN - sumOfN;
        int xPy = (runningSumOfN2 - sumOfN2)/xMy;

        return vector<int>{(xMy+xPy)/2, (xPy-xMy)/2};
    }
};

// n**2
// class Solution {
// public:
//     vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
//         int n = grid.size(),i,j;
//         vector<bool> found(n*n + 1, false);
//         vector<int> ans(2, -1);
//         for (i=0;i<n;++i)
//             for (j=0;j<n;++j)
//                 if (found[grid[i][j]]){
//                     ans[0]=grid[i][j];
//                 } else {
//                     found[grid[i][j]]=true;
//                 }

//         for (i=1;i<=n*n;++i)
//             if (!found[i]){
//                 ans[1]= i;
//                 break;
//             }

//         return ans;
//     }
// };