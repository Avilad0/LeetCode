#include<bits/stdc++.h>
using namespace std;


// beats 81.45% , O(n)
class Solution {
public:
    int removeStones(vector<vector<int>>& stones) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        UnionFind uf;
        for (auto& stone: stones){
            uf.unionSet(stone[0],stone[1]+10001);
        }

        return stones.size()-uf.connectedComponents;
    }

private:
    class UnionFind {
        private:
            unordered_map<int, int> parent;
        public:
            int connectedComponents=0;

            int find (int x) {
                if (parent.find(x)==parent.end()){
                    ++connectedComponents;
                    return parent[x]=x;
                }
                
                if (parent[x]==x) return x;

                return parent[x] = find(parent[x]);
            }

            void unionSet(int x, int y) {
                int rootX = find(x);
                int rootY = find(y);

                if (rootX==rootY) return;

                parent[rootX] = rootY;
                --connectedComponents;
            }
    };
};

// beats 50% :  runtime 60ms [O(n) but data structures can be better used]
// class Solution {
// public:
//     int removeStones(vector<vector<int>>& stones) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         unordered_map<int,unordered_set<int>> rowCoordinateToIndexes, colCoordinateToIndexes, mergedLinks;
//         unordered_set<int> mergedIndices;
//         int maxStonesToRemove=0, i,n=stones.size(), parentIndex, currIndex;
//         queue<int> indexQueues;

//         for (i=0;i<n;++i){
//             rowCoordinateToIndexes[stones[i][0]].insert(i);
//             colCoordinateToIndexes[stones[i][1]].insert(i);
//         }

//         for(i=0;i<n;++i){
//             if (mergedIndices.find(i)==mergedIndices.end()){
//                 parentIndex = i;
//                 indexQueues.push(i);
                
//                 while (!indexQueues.empty()){
//                     currIndex = indexQueues.front();
//                     indexQueues.pop();

//                     if (mergedIndices.find(currIndex)!=mergedIndices.end()) continue;
//                     mergedIndices.insert(currIndex);

//                     if (currIndex!=parentIndex) mergedLinks[parentIndex].insert(currIndex);

//                     for (auto& index: rowCoordinateToIndexes[stones[currIndex][0]]) indexQueues.push(index);
//                     for (auto& index: colCoordinateToIndexes[stones[currIndex][1]]) indexQueues.push(index);
//                 }

//                 maxStonesToRemove += mergedLinks[parentIndex].size();
//             }
//         }

//         return maxStonesToRemove;
//     }
// };


/*
stones = [[0,1],[1,0],[1,1]]

row_maps:
0 = [0,1]
1 = [1,0][1,1]

col_maps:
0 = [1,0]
1 = [0,1][1,1]

links :
[0,1] = [1,1]
[1,0] = [1,1]
[1,1] = [0,1][1,0]

if talking in terms of indices:
row_maps:
0 = 0
1 = 1,2

col_maps
0 = 1
1 = 0,2

links: {0: {2}, 1: {2}, 2:{0,1}}
merged_links : {0:{2,1}}
ans = 2

////

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
for indices:

row_maps:
0: 0,1
1: 2
2: 3,4

col_maps:
0: 0,3
1: 2
2: 1,4

links: {0:{1,3}, 1:{0,4}, 2:{}, 3:{0,4}, 4:{1,3}}
     : {0:{1,3,4}, 2:{}, 4:{1,3}}
     : {0:{1,3,4}, 2:{}}

ans=3
*/