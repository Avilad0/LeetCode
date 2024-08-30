#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int source, int destination, int target) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        vector<vector<pair<int,int>>> graph(n);
        for (auto& e:edges){
            if( e[2]!=-1){
                graph[e[0]].emplace_back(e[1],e[2]);
                graph[e[1]].emplace_back(e[0],e[2]);
            }
        }

        int currShortestDistance = dijkstra(n,source,destination,graph);
        if (currShortestDistance<target) return {};

        bool matchesTarget = (currShortestDistance==target);

        for (auto& edge: edges){
            if (edge[2]!= -1)    continue;

            edge[2]=matchesTarget? INF:1;
            graph[edge[0]].emplace_back(edge[1], edge[2]);
            graph[edge[1]].emplace_back(edge[0], edge[2]);

            if (!matchesTarget){
                int newDistance = dijkstra(n, source, destination, graph);
                if (newDistance<=target){
                    matchesTarget=true;
                    edge[2]+=target-newDistance;
                }
            }
        }

        return matchesTarget? edges : vector<vector<int>>();
    }

private:
    const int INF = 2e9;

    int dijkstra(int& n, int& source, int& destination, vector<vector<pair<int,int>>>& graph){
        vector<int> minDistance(n, INF);
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> minHeap;

        minDistance[source]=0;
        minHeap.emplace(0,source);

        while(!minHeap.empty()){
            auto [nodeDistance,node] = minHeap.top();
            minHeap.pop();

            if (nodeDistance>minDistance[node]) continue;

            for ( auto& [nextNode, nextWeight]: graph[node]){
                if (nodeDistance + nextWeight < minDistance[nextNode]){
                    minDistance[nextNode] = nodeDistance+nextWeight;
                    minHeap.emplace(minDistance[nextNode], nextNode);
                }
            }
        }
        
        return minDistance[destination];
    }
};

// class Solution {
// public:
//     vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int source, int destination, int target) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
//         visited = vector<bool>(n,false);

//         vector<vector<pair<int,int>>> allEdges(n, vector<pair<int,int>>());
//         for (auto& e:edges){
//             allEdges[e[0]].push_back({e[1],e[2]});
//             allEdges[e[1]].push_back({e[0],e[2]});
//         }
//     }

// private:
//     bool isTargetFound = false;
//     vector<bool> visited;

//     void dfs(vector<vector<pair<int,int>>>& allEdges, int& source, int& destination, int& target, int curr, int currWeight, int negatives){
        
//         if ()

//         for(auto& [node, nodeWeight]: allEdges[curr]){
//             if (visited[node]) continue;
//             visited[node]=true;
//             dfs(allEdges, source, destination, target, node, currWeight + nodeWeight);
//             visited[node]=false;
//         }
//     }
// };