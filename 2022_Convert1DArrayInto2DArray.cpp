#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {      
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        if (m*n != original.size()) return vector<vector<int>>();

        vector<vector<int>> newVector(m, vector<int>(n));

        for (int i=0;i<m;++i){
            for (int j=0;j<n;++j){
                newVector[i][j] = original[i*n + j];
            }
        }

        return newVector;
    }
};