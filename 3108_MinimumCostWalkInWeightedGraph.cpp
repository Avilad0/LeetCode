#include<bits/stdc++.h>
using namespace std;

class DisjointSet {
private:
    vector<int> parent, weights;
    int n;
public:
    DisjointSet(int n){
        this->n = n;
        for (int i=0;i<=n; ++i){
            parent.push_back(i);
            weights.push_back(~0);
        }
    }
    
    int getWeight( int x){
        return weights[x];
    }

    int findParent(int x){
        if (parent[x] != x){
            parent[x] = findParent(parent[x]);
        }
        return parent[x];
    }

    void unionByRank(int x, int y, int weight){
        x = findParent(x);
        y = findParent(y);

        weights[x] = weights[y] = weights[x] & weights[y] & weight;
        parent[y] = x;
    }
};

class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        DisjointSet ds(n);

        for (auto& edge: edges){
            ds.unionByRank(edge[0], edge[1], edge[2]);
        }

        vector<int> ans;
        for (auto& q: query){
            int x = ds.findParent(q[0]), y=ds.findParent(q[1]);
            if (x!= y){
                ans.push_back(-1);
            } else {
                ans.push_back(ds.getWeight(x));
            }
        }
        return ans;
    }
};

// class DisjointSet {
// private:
//     vector<int> parent, weights;
//     int n;
// public:
//     DisjointSet(int n){
//         this->n = n;
//         for (int i=0;i<=n; ++i){
//             parent.push_back(i);
//             weights.push_back(-1);
//         }
//     }
    
//     int getWeight( int x){
//         return weights[x];
//     }

//     int findParent(int x){
//         if (parent[x] != x){
//             parent[x] = findParent(parent[x]);
//         }
//         return parent[x];
//     }

//     void unionByRank(int x, int y, int weight){
//         x = findParent(x);
//         y = findParent(y);

//         if (weights[x] == -1 &&  weights[y]==-1){
//             weights[x] = weights[y] = weight;
//             parent[y] = x;
//         } else if (weights[x] == -1){
//             weights[x] = weights[y] = weights[y] & weight;
//             parent[x] = y;
//         } else if (weights[y]==-1){
//             weights[x] = weights[y] = weights[x] & weight;
//             parent[y] = x;
//         } else {
//             weights[x] = weights[y] = weights[x] & weights[y] & weight;
//             parent[y] = x;
//         }
//     }
// };

// class Solution {
// public:
//     vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
//         DisjointSet ds(n);

//         for (auto& edge: edges){
//             ds.unionByRank(edge[0], edge[1], edge[2]);
//         }

//         vector<int> ans;
//         for (auto& q: query){
//             int x = ds.findParent(q[0]), y=ds.findParent(q[1]);
//             if (x!= y){
//                 ans.push_back(-1);
//             } else {
//                 ans.push_back(ds.getWeight(x));
//             }
//         }
//         return ans;
//     }
// };