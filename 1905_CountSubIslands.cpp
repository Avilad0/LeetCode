#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        m=grid1.size();
        n=grid1[0].size();
        int ans=0;

        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(grid2[i][j]==1)  ans+=isSubIsland(grid1,grid2, i,j);
            }
        }

        return ans;
    }

private:
    int m,n;
    vector<pair<int,int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};
    
    bool isSubIsland(vector<vector<int>>& grid1, vector<vector<int>>& grid2, int row, int column){

        if(row<0 || row>=m || column<0 || column>=n) return true;

        if (grid1[row][column]==0){
            if (grid2[row][column]==0) return true;
            else return false;
        }

        if (grid1[row][column]==1 && grid2[row][column]==0) return true;

        grid2[row][column]=0;

        bool isSub =true;
        for(auto& [i,j]: directions){
            isSub &= isSubIsland(grid1, grid2, row+i, column+j);
        }
        return isSub;
    }
};