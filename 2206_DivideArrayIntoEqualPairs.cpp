#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_set<int> set;
        for (auto& num: nums){
            if (set.find(num)==set.end()){
                set.insert(num);
            } else {
                set.erase(num);
            }
        }

        return set.empty();
    }
};

// class Solution {
// public:
//     bool divideArray(vector<int>& nums) {
//         unordered_map<int,bool> map;
//         int count = 0;
//         for (auto& num: nums){
//             map[num] = !map[num];
//             count += map[num];
//         }

//         return count==(nums.size()/2);
//     }
// };