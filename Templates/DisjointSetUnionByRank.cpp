#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
private:
    vector<int> parent, rank;
    int n;
public:
    DisjointSet(int n){
        this->n = n;
        for (int i=0;i<=n; ++i){
            parent.push_back(i);
            rank.push_back(1);
        }
    }

    int findParent(int x){
        if (parent[x] != x){
            parent[x] = findParent(parent[x]);
        }
        return parent[x];
    }

    void unionByRank(int x, int y){
        x = findParent(x);
        y = findParent(y);
        if (x == y) return;

        if (rank[x] < rank[y]){
            parent[x] = y;
        } else if (rank[x] > rank[y]){
            parent[y] = x;
        } else {
            parent[y] = x;
            rank[x]++;
        }
    }
};