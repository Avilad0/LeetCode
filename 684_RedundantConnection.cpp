#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size(),i;
        vector<int> parent;
        for (i=0;i<=n;i++){
            parent.push_back(i);
        }

        for (auto& e : edges){
            if ( ! unionn(parent, e[0],e[1])){
                return e;
            }
        }

        return {};
    }

private:
    int find(vector<int>& parent, int p){
        if (p==parent[p]){
            return p;
        } 

        parent[p] = find(parent, parent[p]);
        return parent[p];
    }

    bool unionn(vector<int>& parent, int x1, int x2){
        x1 = find(parent, x1);
        x2 = find(parent, x2);

        if (x1==x2){
            return false;
        }
        
        parent[x1]=x2;
        
        return true;
    }
};

// class Solution {
// public:
//     vector<int> findRedundantConnection(vector<vector<int>>& edges) {
//         int n = edges.size(),i;
//         vector<int> parent, rank;
//         for (i=0;i<=n;i++){
//             parent.push_back(i);
//             rank.push_back(1);
//         }

//         for (auto& e : edges){
//             if ( ! unionn(parent, rank, e[0],e[1])){
//                 return e;
//             }
//         }

//         return {};
//     }

// private:
//     int find(vector<int>& parent, int p){
//         p= parent[p];

//         while (p!=parent[p]){
//             //shorten find path for the next time;
//             parent[p] = parent[parent[p]];
//             p=parent[p];
//         }

//         return p;
//     }

//     bool unionn(vector<int>& parent, vector<int>& rank, int x1, int x2){
//         x1 = find(parent, x1);
//         x2 = find(parent, x2);

//         if (x1==x2){
//             return false;
//         }

//         if (rank[x1]<rank[x2]){
//             parent[x1]=x2;
//             rank[x2]+=rank[x1];
//         } else{
//             parent[x2]=x1;
//             rank[x1]+=rank[x2];
//         }
//         return true;
//     }
// };




// p = [0,1,2,3,1,4]

// x=5
// x=par[x]
// x=4
// par[4]=par[par[4]]
// p = [0,1,2,3,1,4]
// x=p[4]=1

// 1==p[1]
