#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> sortJumbled(vector<int>& mapping, vector<int>& nums) {
        map<int,vector<int>> sortedMappings;
        int t,n1,i;
        for(auto& n: nums){
            t=0;
            n1=n;
            i=1;
            do{
                t += mapping[(n1%10)]*i;
                n1/=10;
                i*=10;
            } while (n1>0);
            sortedMappings[t].push_back(n);
        }

        i=0;
        for (auto& [_,ns] : sortedMappings){
            for (auto& n : ns) nums[i++]=n;
        }

        return nums;
    }
};

int main(){
    Solution s;
    // vector<int> mapping = {8,9,4,0,2,1,3,5,7,6}, nums = {991,338,38}, ans = s.sortJumbled(mapping, nums);
    // Output: [338,38,991]
    vector<int> mapping = {9,8,7,6,5,4,3,2,1,0}, nums = {0,1,2,3,4,5,6,7,8,9}, ans = s.sortJumbled(mapping, nums);

    for (auto&n : ans) cout<<n<<"  ";

    return 0;
}