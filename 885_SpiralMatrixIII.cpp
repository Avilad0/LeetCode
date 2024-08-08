#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        vector<vector<pair<int,int>>> directions({ {{0,1},{1,0}}, {{0,-1},{-1,0}} });
        int steps=1, i,j,k;

        vector<vector<int>> visitOrder;
        
        while (visitOrder.size()<rows*cols){
            for (i=0;i<2;++i){
                
                for(j=0;j<2;++j){
                    if ( (j==0 && (rStart<0 || rows<=rStart)) ||  (j==1 && (cStart<0 || cols<=cStart))){
                        rStart+= steps*directions[i][j].first;
                        cStart+= steps*directions[i][j].second;
                    } else {

                        for(k=0;k<steps;++k){
                            if (0<=rStart && rStart<rows && 0<=cStart && cStart<cols) visitOrder.push_back({rStart,cStart});
                            rStart+=directions[i][j].first;
                            cStart+=directions[i][j].second;
                        }
                    }
                }
                ++steps;
            }
        }

        return visitOrder;
    }
};