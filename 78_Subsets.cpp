#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> ans;
    int n;
    vector<vector<int>> subsets(vector<int>& nums) {
        n=nums.size();
        addSubsets(nums, 0);

        return ans;
    }

    void addSubsets(vector<int>& nums, int i, vector<int> subset = vector<int>()) {
        if (i==n){
            ans.push_back(subset);
            return;
        }

        addSubsets(nums, i+1,subset);
        subset.push_back(nums[i]);
        addSubsets(nums, i+1,subset);


    }
};

int main(){
    Solution s;
    
    vector<int> in = {1,2,3};
    s.subsets(in);
    
    for (vector<int> &i : s.ans){
        for (int &j: i){
            cout<<j<<" ";
        }
        cout<<"\n";
    }
    return 0;
}