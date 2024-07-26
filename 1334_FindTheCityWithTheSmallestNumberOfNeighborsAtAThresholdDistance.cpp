#include<bits/stdc++.h>
using namespace std;


class Solution {

public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        vector<vector<int>> distanceMatrix(n, vector<int>(n, 10001));

        for (int i=0;i<n;++i) distanceMatrix[i][i]=0;

        for (auto& edge : edges){
            distanceMatrix[edge[0]][edge[1]] = edge[2];
            distanceMatrix[edge[1]][edge[0]] = edge[2];
        }

        for (int k=0;k<n;k++){
            for (int i=0;i<n;++i){
                for (int j=0;j<=i;++j){
                    distanceMatrix[i][j] = min(distanceMatrix[i][j], distanceMatrix[i][k] + distanceMatrix[k][j]);
                    distanceMatrix[j][i] = distanceMatrix[i][j];
                }
            }
        }

        int fewestReachableCity, fewestReachableCityCount = INT_MAX, count;

        for (int i=0;i<n;++i){
            count=0;
            for (int j=0; j<n; ++j){
                if (distanceMatrix[i][j]<=distanceThreshold)count++;
            }

            if (count<= fewestReachableCityCount){
                fewestReachableCity = i;
                fewestReachableCityCount = count;
            }
        }

        return fewestReachableCity;
    }
};