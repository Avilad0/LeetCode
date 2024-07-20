#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        vector<vector<int>> matrix(rowSum.size(), vector<int>(colSum.size(),0));

        // for (int i = 0; i < rowSum.size(); i++) {
        //     for (int j = 0; j < colSum.size(); j++) {
        //         matrix[i][j] = min(rowSum[i], colSum[j]);

        //         rowSum[i] -= matrix[i][j];
        //         colSum[j] -= matrix[i][j];
        //     }
        // }

        int i = 0, j = 0;
        while (i < rowSum.size() && j < colSum.size()) {
            matrix[i][j] = min(rowSum[i], colSum[j]);

            rowSum[i] -= matrix[i][j];
            colSum[j] -= matrix[i][j];

            rowSum[i] == 0 ? i++ : j++;
        }

        return matrix;
    }
};


// Input: rowSum = [5,7,10], colSum = [8,6,8]
// Output: [[0,5,0],
//          [6,1,0],
//          [2,0,8]]

// 5 0 0
// 3 4 0
// 0 2 8