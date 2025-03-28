#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> maxPoints(vector<vector<int>>& grid, vector<int>& queries) {
        int m = grid.size(), n= grid[0].size(), k = queries.size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        priority_queue<pair<int,int> , vector<pair<int,int>>, greater<>> queryMinHeap;
        
        for (int i=0; i<k; ++i){
            queryMinHeap.push( pair<int,int>({queries[i], i}) );
        }        
        
        priority_queue<vector<int>, vector<vector<int>>, greater<>> pq;
        pq.push(vector<int>{grid[0][0],0,0});
        visited[0][0]=true;
        
        const vector<pair<int,int>> directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        
        vector<int> ans(k, 0);
        int currSum = 0, i,j, ni, nj;
        while (!pq.empty()){
            while (!queryMinHeap.empty() && pq.top()[0] >= queryMinHeap.top().first){
                ans[queryMinHeap.top().second] = currSum;
                queryMinHeap.pop();
            }
            
            if (queryMinHeap.empty())  break;

            i= pq.top()[1];
            j = pq.top()[2];
            pq.pop();
            currSum++;

            for (auto& [x, y] : directions) {
                ni = i + x;
                nj = j + y;
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && !visited[ni][nj]) {
                    visited[ni][nj] = true;
                    pq.push(vector<int>{grid[ni][nj], ni, nj});
                }
            }
        }

        while (!queryMinHeap.empty()){
            ans[queryMinHeap.top().second] = currSum;
            queryMinHeap.pop();
        }

        return ans;
    }
};

int main(){
    Solution s;
    vector<vector<int>> grid = {{1,2,3},{2,5,7},{3,5,1}};
    vector<int> queries = {5,6,2}, ans = s.maxPoints(grid, queries); //Output: [5,8,1]

    return 0;
}