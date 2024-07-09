#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        int currentTime = 0;
        double waitTime = 0;

        for (auto& c: customers){
            if (currentTime<c[0]){
                currentTime = c[0] + c[1];
            } else {
                currentTime+=c[1];
            }
            waitTime += currentTime - c[0];
        }
        
        return waitTime/customers.size();
    }
};