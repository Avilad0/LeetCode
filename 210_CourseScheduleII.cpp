#include<bits/stdc++.h>
using namespace std;

class Solution {
    vector<bool> added, visited;
    vector<int> order;
    vector<vector<int>> adjList;
    bool dfs(int numCourses, int node){
        if (added[node])    return true;

        if (visited[node]) return false;
        visited[node]=true;

        for (auto& neighbor: adjList[node]){
            if (! dfs(numCourses, neighbor))    
                return false;
        }

        
        order.push_back(node);
        added[node] =true;
        
        visited[node]=false;
        return true;
    }

public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        
        adjList.resize(numCourses, vector<int>());     //course: [...prereqs]
        added.resize(numCourses, false);
        visited.resize(numCourses, false);
        
        for (auto& p: prerequisites)    adjList[p[0]].emplace_back(p[1]);

        for (int i=0;i<numCourses; ++i){
            if (! dfs(numCourses, i)){
                return vector<int>{};
            }
        }

        return order;
    }
};

int main(){
    Solution s;
    int n=2;
    vector<vector<int>> prereq = {{1,0}};
    for (int x: s.findOrder(n, prereq)) 
        cout<<x<<" ";  //Output: [0,1]))
    return 0;
}