#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<string>& logs) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int distance =0;
        for (auto& l:logs){
                        
            if ( l == "../"){
                distance = max(0,distance-1);                
            } else if (l!="./"){
                ++distance;
            }
        }        

        return distance;
    }
};