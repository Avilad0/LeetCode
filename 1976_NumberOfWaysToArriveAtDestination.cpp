#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countPaths(int n, vector<vector<int>>& roads) {
        const int MOD = 1e9 + 7;

        vector<vector<pair<int, int>>> adjList(n, vector<pair<int, int>>());
        for (auto road : roads) {
            adjList[road[0]].emplace_back(road[1], road[2]);
            adjList[road[1]].emplace_back(road[0], road[2]);
        }

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> minHeap;
        minHeap.emplace(0, 0);

        vector<long long> minDist(n, LLONG_MAX);
        minDist[0] = 0;

        vector<int> waysToReach(n, 0);
        waysToReach[0] = 1;

        while (!minHeap.empty()){
            long long currDist = minHeap.top().first;
            int currNode = minHeap.top().second;
            minHeap.pop();

            if (currDist > minDist[currNode]) {
                continue;
            }

            for (auto& [neighbour, weight] : adjList[currNode]) {
                if (currDist + weight < minDist[neighbour]) {
                    minDist[neighbour] = currDist + weight;
                    minHeap.emplace(minDist[neighbour], neighbour);
                    waysToReach[neighbour] = waysToReach[currNode];
                } else if (currDist + weight == minDist[neighbour]) {
                    waysToReach[neighbour] = (waysToReach[neighbour] + waysToReach[currNode]) % MOD;
                }
            }
        }

        return waysToReach[n - 1];
    }
};