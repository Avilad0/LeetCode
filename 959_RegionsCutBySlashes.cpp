#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int n=grid.size(), regions=0, i=0, j;
        vector<vector<int>> newGrid(n*3,vector<int>(n*3,0));

        for(;i<n;++i){
            for(j=0;j<n;++j){
                if (grid[i][j]=='\\'){
                    newGrid[i*3][j*3]=1;
                    newGrid[i*3 +1][j*3 +1]=1;
                    newGrid[i*3 +2][j*3 +2]=1;
                } else if(grid[i][j]=='/'){
                    newGrid[i*3][j*3 + 2]=1;
                    newGrid[i*3 +1][j*3 +1]=1;
                    newGrid[i*3 +2][j*3]=1;
                }
            }
        }

        n*=3;
        for(i=0;i<n;++i){
            for(j=0;j<n;++j){
                if (newGrid[i][j]==0){
                    floodFill(newGrid, n, i, j);
                    regions++;
                }
            }
        }

        return regions;
    }

private:
    const vector<vector<int>> DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    void floodFill(vector<vector<int>>& newGrid, int& n, int row, int col){
        queue<pair<int,int>> q;
        newGrid[row][col]=1;
        q.push({row,col});
        
        while (!q.empty()){
            auto [currRow, currCol] = q.front();
            q.pop();
            for(auto& d:DIRECTIONS){
                int newRow = currRow + d[0], newCol = currCol + d[1];
                if (0<=newRow && newRow<n && 0<=newCol && newCol<n && newGrid[newRow][newCol]==0){
                    newGrid[newRow][newCol]=1;
                    q.push({newRow,newCol});
                }
            }
        }
    }
};