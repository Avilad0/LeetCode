#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> directions(n, vector<int>());

        for (auto& e: edges){
            directions[e[0]].push_back(e[1]);
        }

        vector<vector<int>> ancestors(n, vector<int>());
        for(int i=0;i<n;++i){
            dfs(directions, i, i, ancestors);
        }
        
        return ancestors;
    }

    void dfs(vector<vector<int>>& directions, int& parent, int& current, vector<vector<int>>& ancestors){
        for (auto& d:directions[current]){
            if (ancestors[d].empty() || ancestors[d].back() != parent) {
                ancestors[d].push_back(parent);
                dfs(directions, parent, d, ancestors);
            }
        }
    }
};



// n = 8, 
// edgeList = [ [0,3], [0,4], [1,3], [2,4], [2,7], [3,5],[3,6],[3,7],[4,6]]
// Output:    [ [], [], [], [0,1], [0,2], [0,1,3], [0,1,2,3,4], [0,1,2,3]]

// 0 > 3,4
// 1 > 3
// 2 > 4,7
// 3 > 5,6,7
// 4 > 6

// 0 > 
// 1 > 
// 2 > 
// 3 > 0,1
// 4 > 0,2
// 5 > 3
// 6 > 3,4
// 7 > 2,3




// //////////////////////

// Input: n = 5, edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
// Output: [[],[0],[0,1],[0,1,2],[0,1,2,3]]


// 0 > 
// 1 > 0
// 2 > 0,1
// 3 > 0,1,2
// 4 > 0,1,2,3