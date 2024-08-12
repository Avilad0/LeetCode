#include<bits/stdc++.h>
using namespace std;


class KthLargest {
private:

    int k;
    priority_queue<int> numsQueue; 

public:
    KthLargest(int k, vector<int>& nums) : k(k){
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        for (auto& n: nums) numsQueue.push(-n);
    }
    
    int add(int val) {
        numsQueue.push(-val);

        while (numsQueue.size()!=k) numsQueue.pop();

        return -numsQueue.top();
    }
};


/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */