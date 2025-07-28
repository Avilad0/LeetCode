#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    int n, maxOR = 0;
    unordered_map<int, int> memo;

    int dfs(const vector<int>& nums, int index, int currOR){
        if (index == n) return int(currOR == maxOR);

        int key = (currOR<<4) | index;
        if (memo.find(key)!=memo.end()) return memo[key];

        memo[key] = dfs(nums, index+1, currOR) + dfs(nums, index+1, currOR|nums[index]);

        return memo[key];

    }
public:
    int countMaxOrSubsets(vector<int>& nums) {
        for (auto& num: nums)   maxOR |= num;

        n = nums.size();

        return dfs(nums, 0, 0);
    }
};