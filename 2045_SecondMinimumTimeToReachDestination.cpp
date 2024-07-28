#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
        vector<vector<int>> adj(n + 1);
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        queue<pair<int, int>> q;
        q.push({1, 1});
        vector<int> dist1(n + 1, -1), dist2(n + 1, -1);
        dist1[1] = 0;

        while (!q.empty()) {
            auto [node, freq] = q.front();
            q.pop();

            int timeTaken = freq == 1 ? dist1[node] : dist2[node];
            if ((timeTaken / change) % 2) {
                timeTaken = change * (timeTaken / change + 1) + time;
            } else {
                timeTaken = timeTaken + time;
            }

            for (auto& neighbor : adj[node]) {
                if (dist1[neighbor] == -1) {
                    dist1[neighbor] = timeTaken;
                    q.push({neighbor, 1});
                } else if (dist2[neighbor] == -1 && dist1[neighbor] != timeTaken) {
                    if (neighbor == n) return timeTaken;
                    dist2[neighbor] = timeTaken;
                    q.push({neighbor, 2});
                }
            }
        }
        return 0;
    }
};

// class Solution {
// public:
//     int secondMinimum(int n, vector<vector<int>>& edges, int time, int change) {
//         unordered_map<int,vector<int>> edgesMap;
//         for (auto& e:edges){
//             edgesMap[e[0]].push_back(e[1]);
//             edgesMap[e[1]].push_back(e[0]);
//         }

//         queue<pair<int,int>> bfsQueue;
//         bfsQueue.emplace(1, 0);
//         vector<int> found(n+1, 0);
//         vector<int> minEdgesCount(n+1);
//         int currVertex, edgesCount, secondMinEdgesCount=-1;

//         while (!bfsQueue.empty()){
//             currVertex = bfsQueue.front().first;
//             edgesCount = bfsQueue.front().second;
//             bfsQueue.pop();
            
//             if (currVertex==n && found[n]>0 && minEdgesCount[n]<edgesCount){
//                     secondMinEdgesCount = edgesCount;
//                     break;
//             }

//             if (found[currVertex]>1){
//                 continue;
//             }

//             ++found[currVertex];
//             minEdgesCount[currVertex] = edgesCount;
//             ++edgesCount;
//             for (auto& v: edgesMap[currVertex]){
//                 if (found[v]==0 || (found[v]<2 && edgesCount>minEdgesCount[v])) bfsQueue.emplace(v, edgesCount);
//             }
//         }
        
//         if (secondMinEdgesCount==-1) secondMinEdgesCount = minEdgesCount[n]+2;

//         int secondMinimumTime = 0;
//         for(;secondMinEdgesCount>0; --secondMinEdgesCount){
//             if ( (secondMinimumTime/change)%2 == 0 ){
//                 secondMinimumTime+=time;
//             } else {
//                 secondMinimumTime += change - (secondMinimumTime%change) + time;
//             }
//         }

//         return secondMinimumTime;
//     }
// };


int main(){
    Solution s;
    // int n = 2, time = 3, change = 2;
    // vector<vector<int>> edges = {{1,2}};  // Output: 11

    int n = 5, time = 3, change = 5;
    vector<vector<int>> edges = {{1,2},{1,3},{1,4},{3,4},{4,5}};  // Output: 13
    cout<<s.secondMinimum(n,edges, time, change);
    return 0;
}