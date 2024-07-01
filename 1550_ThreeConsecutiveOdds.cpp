#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int counter=0;
        for (auto& n: arr){
            if (n%2==0){
                counter=0;
            } else {
                if (counter==2){
                    return true;
                }
                ++counter;
            }
        }
        return false;
    }
};