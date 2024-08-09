#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        int m=grid.size()-2, n=grid[0].size()-2, i=0, j, ans=0;

        for (;i<m;++i){
            for (j=0;j<n;++j){
                if (isMagicSquare(grid, i, j)) ++ans; 
            }
        }
        return ans;
    }

private:
    bool isMagicSquare(vector<vector<int>>& grid, int row, int column){

        vector<bool> visited({true,false,false,false,false,false,false,false,false,false});
        for (int i=0;i<3;++i){
            for (int j=0;j<3;++j){
                if (grid[row+i][column+j]<1 || 9<grid[row+i][column+j] || visited[grid[row+i][column+j]]) return false;
                
                visited[grid[row+i][column+j]] = true;
            }
        }

        int sum = grid[row][column] + grid[row+1][column+1] + grid[row+2][column+2];

        if ( sum!=15
                || sum != grid[row][column+2] + grid[row+1][column+1] + grid[row+2][column] 
                || sum != grid[row][column] + grid[row][column+1] + grid[row][column+2]
                || sum != grid[row+1][column] + grid[row+1][column+1] + grid[row+1][column+2]
                || sum != grid[row+2][column] + grid[row+2][column+1] + grid[row+2][column+2]
                || sum != grid[row][column] + grid[row+1][column] + grid[row+2][column]
                || sum != grid[row][column+1] + grid[row+1][column+1] + grid[row+2][column+1]
                || sum != grid[row][column+2] + grid[row+1][column+2] + grid[row+2][column+2])  
            return false;

        return true;
    }
};

int main(){
    Solution s;
    // vector<vector<int>> grid( { {6,1,8}, {7,5,3}, {2,9,4} });
    vector<vector<int>> grid( { {3,2,9,2,7},{6,1,8,4,2},{7,5,3,2,7},{2,9,4,9,6},{4,3,8,2,5}});

    cout<<s.numMagicSquaresInside(grid);
    return 0;
}