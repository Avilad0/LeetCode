#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int pos=0, neg=0;
        for(auto& num: nums){
            if (num>0)  pos++;
            else if(num<0)  neg++;
        }

        return pos>neg? pos: neg;
    }
};