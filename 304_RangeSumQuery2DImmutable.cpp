#include<bits/stdc++.h>
using namespace std;

class NumMatrix {
private:
    vector<vector<int>> prefixSum;
    int m,n;
public:
    NumMatrix(vector<vector<int>>& matrix) {
        m = matrix.size();
        n = matrix[0].size();
        prefixSum.resize(m+1, vector<int>(n+1,0));

        int i,j;
        for (i=1;i<=m;++i){
            for (j=1;j<=n;++j){
                prefixSum[i][j] = matrix[i-1][j-1] + prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        return prefixSum[row2+1][col2+1] - prefixSum[row1][col2+1] - prefixSum[row2+1][col1] + prefixSum[row1][col1];
    }
};

// class NumMatrix {
// private:
//     vector<vector<int>> prefixSum;
//     int m,n;
// public:
//     NumMatrix(vector<vector<int>>& matrix) {
//         m = matrix.size();
//         n = matrix[0].size();
//         for (int i=0;i<m;++i){
//             prefixSum.push_back({matrix[i][0]});
//             for (int j=1;j<n;++j){
//                 prefixSum[i].push_back(prefixSum[i][j-1]+matrix[i][j]);
//             }
//         }

//         for (int j=0;j<n;++j){
//             for (int i=1;i<m;++i){
//                 prefixSum[i][j] += prefixSum[i-1][j];
//             }
//         }
//     }
    
//     int sumRegion(int row1, int col1, int row2, int col2) {
//         int sum = prefixSum[row2][col2];

//         if (row1>0){
//             sum -= prefixSum[row1-1][col2];
//         }

//         if (col1>0){
//             sum -= prefixSum[row2][col1-1];
//             if (row1>0){
//                 sum += prefixSum[row1-1][col1-1];
//             }
//         }        

//         return sum;
//     }
// };


/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */