#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    vector<int> parent, size;
    
    int findParent(int x){
        if (parent[x]!=x)   parent[x] = findParent(parent[x]);

        return parent[x];
    }

    void unionBySize(int x, int y){
        x = findParent(x);
        y = findParent(y);

        if (x == y) return;

        if (size[y]> size[x]){
            parent[x] = y;
            size[y] += size[x];
        } else {
            parent[y] = x;
            size[x] += size[y];
        }
    }
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {        
        for (int i=0; i<n; ++i){
            parent.push_back(i);
            size.push_back(1);
        }

        for (auto& e: edges){
            unionBySize(e[0], e[1]);
        }

        unordered_map<int, int> edgesCount;
        for (auto& e: edges){
            edgesCount[findParent(e[0])] ++;
        }

        int completeCount=0;
        for (int i=0;i<n;++i){
            if (findParent(i)==i){
                if (edgesCount[i] == (size[i]*(size[i]-1))/2){
                    completeCount++;
                }
            }            
        }

        return completeCount;
    }
};

// class Solution {
// private:
//     vector<int> parent, size;
//     unordered_set<int> uniqueParent;
    
//     int findParent(int x){
//         if (parent[x]!=x)   parent[x] = findParent(parent[x]);

//         return parent[x];
//     }

//     void unionBySize(int x, int y){
//         x = findParent(x);
//         y = findParent(y);

//         if (x == y) return;

//         if (size[y]> size[x]){
//             parent[x] = y;
//             size[y] += size[x];
//             uniqueParent.erase(x);
//         } else {
//             parent[y] = x;
//             size[x] += size[y];
//             uniqueParent.erase(y);
//         }
//     }
// public:
//     int countCompleteComponents(int n, vector<vector<int>>& edges) {        
//         vector<int> edgesCount;
//         for (int i=0; i<n; ++i){
//             parent.push_back(i);
//             uniqueParent.insert(i);
//             size.push_back(1);
//             edgesCount.push_back(0);
//         }

//         for (auto& e: edges){
//             unionBySize(e[0], e[1]);
//             edgesCount[e[0]]++;
//             edgesCount[e[1]]++;
//         }

//         for (int i=0; i<n; ++i){
//             if (uniqueParent.find(parent[i]) != uniqueParent.end()){
//                 if (edgesCount[i] != size[parent[i]]-1){
//                     uniqueParent.erase(parent[i]);
//                 }
//             }
//         }

//         return uniqueParent.size();
//     }
// };

// class Solution {
// private:
//     vector<int> parent, size;
    
//     int findParent(int x){
//         if (parent[x]!=x)   parent[x] = findParent(parent[x]);

//         return parent[x];
//     }

//     void unionBySize(int x, int y){
//         x = findParent(x);
//         y = findParent(y);

//         if (x == y) return;

//         if (size[y]> size[x]){
//             parent[x] = y;
//             size[y] += size[x];
//         } else {
//             parent[y] = x;
//             size[x] += size[y];
//         }
//     }
// public:
//     int countCompleteComponents(int n, vector<vector<int>>& edges) {        
//         vector<int> edgesCount;
//         for (int i=0; i<n; ++i){
//             parent.push_back(i);
//             size.push_back(1);
//             edgesCount.push_back(0);
//         }

//         for (auto& e: edges){
//             unionBySize(e[0], e[1]);
//             edgesCount[e[0]]++;
//             edgesCount[e[1]]++;
//         }

//         unordered_map<int,int> parentToSize;
//         for (int i=0; i<n; ++i){
//             parentToSize[findParent(i)]++;
//         }

//         for (int i=0; i<n; ++i){
//             if (parentToSize.find(parent[i]) != parentToSize.end()){
//                 if (edgesCount[i] != parentToSize[parent[i]]-1){
//                     parentToSize.erase(parent[i]);
//                 }
//             }
//         }

//         return parentToSize.size();
//     }
// };

int main(){
    Solution s;
    vector<vector<int>> edges = {{0,1},{0,2},{1,2},{3,4}};
    cout<<s.countCompleteComponents(6, edges)<<endl; 
    return 0;
}