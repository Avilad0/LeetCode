#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        vector<int> rowMin(matrix.size()), columnMax(matrix[0].size());
        int i,j, maxx, maxxIndex;
        for (j=0;j<matrix[0].size();++j){
            maxx = 0;
            for (i=0;i<matrix.size();++i){
                if(maxx<matrix[i][j]){
                    maxx = matrix[i][j];
                    maxxIndex = i;
                }
            }
            if (maxx == *min_element(matrix[maxxIndex].begin(), matrix[maxxIndex].end())) return {maxx};
        }

        return {};
    }
};