#include<bits/stdc++.h>
using namespace std;

class Solution {

public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        
        vector<int> min_dist(n,INT_MAX);
        min_dist[src]=0;

        for (int i=0;i<=k;i++){
            vector<int> temp_dist(min_dist);

            for (auto& f: flights){
                if (min_dist[f[0]]==INT_MAX){
                    continue;
                }

                if (min_dist[f[0]]+f[2] < temp_dist[f[1]]){
                    temp_dist[f[1]] = min_dist[f[0]]+f[2];
                }
            }

            min_dist = temp_dist;
        }

        return min_dist[dst]==INT_MAX?-1: min_dist[dst];
    }
};

// int main(){
//     bool b = INT_MAX==INT_MAX;
//     cout<<boolalpha<<b;
//     return 0;
// }

// class Solution {
// private:
//     int min_cost = INT_MAX;
//     map<int, vector<vector<int>>> paths;
    
//     void travel(int& dst, int k, int curr, int cost){ 
//         if ((k==0 && curr!=dst) || cost>min_cost){
//             return;
//         }
//         if (curr==dst){
//             if (cost<min_cost){
//                 min_cost=cost;
//             }
//             return;
//         }

//         for (auto& f:paths[curr]){
//             travel(dst, k-1, f[1], cost+f[2]);
//         }
//     }


// public:
//     int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {

//         for (auto& f:flights){
//             paths[f[0]].push_back(f);
//         }

//         travel(dst, k+1, src,0);
//         return min_cost==INT_MAX?-1:min_cost;
//     }
// };