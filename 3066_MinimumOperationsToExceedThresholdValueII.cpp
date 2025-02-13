#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        priority_queue<long, vector<long>, greater<long>> pq(nums.begin(), nums.end());

        int operations = 0;
        long x,y;

        while (pq.size()>1 && pq.top()<k){
            x = pq.top(); 
            pq.pop();
            y = pq.top();
            pq.pop();

            pq.emplace(2*x + y);
            ++operations;
        }

        return operations;
    }
};