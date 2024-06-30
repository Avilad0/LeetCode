#include<bits/stdc++.h>
using namespace std;

class UnionSet{
public:
    vector<int> parent;
    int n;

    UnionSet(int n){
        this->n = n;
        for (int i=0; i<=n; ++i){
            parent.push_back(i);
        }
    }

    int find(int x){
        if (x==parent[x]){
            return x;
        }

        parent[x]=find(parent[x]);
        return parent[x];
    }

    int unionn(int x1, int x2){
        x1= find(x1);
        x2= find(x2);

        if (x1==x2) return 0;

        parent[x2]= x1;
        
        --n;
        return 1;
    }
};

class Solution {
public:
    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {

        UnionSet A(n), B(n);
        int edgesCount=0;

        for (auto& e: edges){
            if (e[0]==3){
                edgesCount +=  (A.unionn(e[1],e[2]) | B.unionn(e[1],e[2]));
            }
        }

        if (A.n==1 && B.n==1){
            return edges.size() - edgesCount;
        }

        for (auto& e: edges){
            if (e[0]==1)  edgesCount+= A.unionn(e[1],e[2]);
            else if (e[0]==2) edgesCount+= B.unionn(e[1],e[2]);
        }

        if (A.n==1 && B.n==1){
            return edges.size() - edgesCount;
        }

        return -1;
    }
};




// class UnionSet{
// public:
//     vector<int> parent, rank;
//     int n;

//     UnionSet(int n){
//         this->n = n;
//         for (int i=0; i<=n; ++i){
//             parent.push_back(i);
//             rank.push_back(1);
//         }
//     }

//     int find(int x){
//         if (x==parent[x]){
//             return x;
//         }

//         parent[x]=find(parent[x]);
//         return parent[x];
//     }

//     int unionn(int x1, int x2){
//         x1= find(x1);
//         x2= find(x2);

//         if (x1==x2) return 0;

//         if (rank[x1]<rank[x2]){
//             parent[x1]=x2;
//             rank[x2]+=rank[x1];
//         } else {
//             parent[x2]= x1;
//             rank[x1]+=rank[x2];
//         }

//         --n;
//         return 1;
//     }
// };

// class Solution {
// public:
//     int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {

//         UnionSet A(n), B(n);
//         int edgesCount=0;

//         for (auto& e: edges){
//             if (e[0]==3){
//                 edgesCount +=  (A.unionn(e[1],e[2]) | B.unionn(e[1],e[2]));
//             }
//         }

//         if (A.n==1 && B.n==1){
//             return edges.size() - edgesCount;
//         }

//         for (auto& e: edges){
//             if (e[0]==1)  edgesCount+= A.unionn(e[1],e[2]);
//             else if (e[0]==2) edgesCount+= B.unionn(e[1],e[2]);
//         }

//         if (A.n==1 && B.n==1){
//             return edges.size() - edgesCount;
//         }

//         return -1;
//     }
// };
