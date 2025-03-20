#include <bits/stdc++.h>
using namespace std;

class DisjointSet {
private:
    vector<int> parent, size;
    int n;
public:
    DisjointSet(int n){
        this->n = n;
        for (int i=0;i<=n; ++i){
            parent.push_back(i);
            size.push_back(1);
        }
    }

    int findParent(int x){
        if (parent[x] != x){
            parent[x] = findParent(parent[x]);
        }
        return parent[x];
    }

    void unionBySize(int x, int y){
        x = findParent(x);
        y = findParent(y);
        if (x == y) return;

        if (size[x] < size[y]){
            parent[x] = y;
            size[y] += size[x];
        } else {
            parent[y] = x;
            size[x] += size[y];
        }
    }
};