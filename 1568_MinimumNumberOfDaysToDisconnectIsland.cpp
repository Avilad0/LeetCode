#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDays(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int rows = grid.size(), cols = grid[0].size();
        ArticulationPointInfo apInfo(false, 0);
        int landCells = 0, islandCount = 0;

        vector<vector<int>> discoveryTime(rows,vector<int>(cols, -1));  // Time when a cell is first discovered
        vector<vector<int>> lowestReachable(rows,vector<int>(cols, -1));  // Lowest discovery time reachable from the subtree rooted at this cell
        vector<vector<int>> parentCell(rows, vector<int>(cols, -1));  // Parent of each cell in DFS tree

        // Traverse the grid to find islands and articulation points
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    landCells++;
                    if (discoveryTime[i][j] == -1) {  // If not yet visited
                        // Start DFS for a new island
                        findArticulationPoints(grid, i, j, discoveryTime,lowestReachable, parentCell,apInfo);
                        islandCount++;
                    }
                }
            }
        }

        // Determine the minimum number of days to disconnect the grid
        if (islandCount == 0 || islandCount >= 2)   return 0; // Already disconnected or no land

        if (landCells == 1) return 1;  // Only one land cell

        if (apInfo.hasArticulationPoint) return 1;  // An articulation point exists

        return 2;      // Need to remove any two land cells
    }

private:
    // Directions for adjacent cells: right, down, left, up
    const vector<vector<int>> DIRECTIONS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    struct ArticulationPointInfo {
        bool hasArticulationPoint;
        int time;

        ArticulationPointInfo(bool hasArticulationPoint, int time)
            : hasArticulationPoint(hasArticulationPoint), time(time) {}
    };
    
    void findArticulationPoints(vector<vector<int>>& grid, int row, int col,
                                vector<vector<int>>& discoveryTime,
                                vector<vector<int>>& lowestReachable,
                                vector<vector<int>>& parentCell,
                                ArticulationPointInfo& apInfo) {
        int rows = grid.size(), cols = grid[0].size();
        discoveryTime[row][col] = apInfo.time;
        apInfo.time++;
        lowestReachable[row][col] = discoveryTime[row][col];
        int children = 0;

        // Explore all adjacent cells
        for (const auto& direction : DIRECTIONS) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (isValidLandCell(grid, newRow, newCol)) {
                if (discoveryTime[newRow][newCol] == -1) {
                    children++;
                    parentCell[newRow][newCol] =
                        row * cols + col;  // Set parent
                    findArticulationPoints(grid, newRow, newCol, discoveryTime,
                                           lowestReachable, parentCell, apInfo);

                    // Update lowest reachable time
                    lowestReachable[row][col] =
                        min(lowestReachable[row][col],
                            lowestReachable[newRow][newCol]);

                    // Check for articulation point condition
                    if (lowestReachable[newRow][newCol] >=
                            discoveryTime[row][col] &&
                        parentCell[row][col] != -1) {
                        apInfo.hasArticulationPoint = true;
                    }
                } else if (newRow * cols + newCol != parentCell[row][col]) {
                    // Update lowest reachable time for back edge
                    lowestReachable[row][col] =
                        min(lowestReachable[row][col],
                            discoveryTime[newRow][newCol]);
                }
            }
        }

        // Root of DFS tree is an articulation point if it has more than one
        // child
        if (parentCell[row][col] == -1 && children > 1) {
            apInfo.hasArticulationPoint = true;
        }
    }

    // Check if the given cell is a valid land cell
    bool isValidLandCell(const vector<vector<int>>& grid, int row, int col) {
        int rows = grid.size(), cols = grid[0].size();
        return row >= 0 && col >= 0 && row < rows && col < cols &&
               grid[row][col] == 1;
    }
};




// class Solution {
// public:
//     int minDays(vector<vector<int>>& grid) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         m=grid.size(), n=grid[0].size();
//         int minDays=0, i=0,j, neighbours;
//         bool found=false;


//         for (;i<m;++i){
//             for (j=0;j<n;++j){
//                 if (grid[i][j]==1) {
//                     if (found) return 0; //already disjoint islands
//                     found=true;
//                     visitNeighbours(grid, i, j);
//                 }
//             }
//         }

//         if (!found) return 0; //no islands;
        
//         //wrong condition
//         //if (uniqueNeighbourValuesFreq.find(2)!=uniqueNeighbourValuesFreq.end() && uniqueNeighbourValuesFreq[2]==1) return 1; //2 clusters connected with just 1 cell; 

//         if (uniqueNeighbourValuesFreq.find(1)!=uniqueNeighbourValuesFreq.end() 
//                 && uniqueNeighbourValuesFreq.find(2)!=uniqueNeighbourValuesFreq.end()) return 1; //can be disconnected with only
        
//         return 2; //atmost 2 removals;  
//     }

// private:
//     const vector<vector<int>> DIRECTIONS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
//     unordered_map<int,int> uniqueNeighbourValuesFreq;
//     int m,n;

//     void visitNeighbours(vector<vector<int>>& grid, int row, int col){
        
//         grid[row][col]=-1;
//         int neighbours=0;
//         for(auto& d:DIRECTIONS){
//             int newRow = row + d[0], newCol = col + d[1];
//             if (0<=newRow && newRow<m && 0<=newCol && newCol<n){
                
//                 if (grid[newRow][newCol]!=0) ++neighbours;
                
//                 if (grid[newRow][newCol]==1) visitNeighbours(grid,newRow,newCol);
//             }
//         }
//         ++uniqueNeighbourValuesFreq[neighbours];
//     }
// };

// above fails in
// [[1,1,0,1,1],
//  [1,1,1,1,1],
//  [1,1,0,1,1],
//  [1,1,0,1,1]]










    // void visitNeighbours(vector<vector<int>>& grid, int row, int col){
    //     queue<pair<int,int>> q;
    //     grid[row][col]=-1;
    //     q.push({row,col});
        
    //     while (!q.empty()){
    //         auto [currRow, currCol] = q.front();
    //         q.pop();
    //         for(auto& d:DIRECTIONS){
    //             int newRow = currRow + d[0], newCol = currCol + d[1];
    //             if (0<=newRow && newRow<m && 0<=newCol && newCol<n && grid[newRow][newCol]==1){
    //                 grid[newRow][newCol]=-1;
    //                 q.push({newRow,newCol});
    //             }
    //         }
    //     }
    // }