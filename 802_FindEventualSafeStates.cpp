#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    bool dfsIsInCyle(vector<vector<int>>& graph, int node, vector<bool>& inCycle, vector<bool>& visited){
        if (inCycle[node])    return true;

        if (visited[node])  return false;

        inCycle[node] = true;
        visited[node] = true;

        for (auto& neighbor: graph[node])
            if (dfsIsInCyle(graph, neighbor, inCycle, visited))
                return true;

        
        return inCycle[node] = false;
    }

public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<bool> inCycle(n, false), visited(n, false);

        for (int i=0; i<n; ++i){
            dfsIsInCyle(graph, i, inCycle, visited);
        }

        vector<int> safeNodes;
        for (int i=0; i<n; ++i)
            if (!inCycle[i])
                safeNodes.emplace_back(i);

        return safeNodes;
    }
};