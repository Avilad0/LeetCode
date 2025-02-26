#include<bits/stdc++.h>
using namespace std;

//same as below with little tweeks for initial calculation as 0 as minn and maxx to take care of all positive or negative
class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int maxx = 0, minn =0, summ =0;

        for (auto& num: nums){
            summ+=num;
            if (summ>maxx)  maxx = summ;
            if (summ<minn)  minn = summ;
        }

        return maxx-minn;
    }
};
    

// class Solution {
// public:
//     int maxAbsoluteSum(vector<int>& nums) {
//         int maxx = INT_MIN, minn = INT_MAX, summ =0;

//         for (auto& num: nums){
//             summ+=num;
//             if (summ>maxx)  maxx = summ;
//             if (summ<minn)  minn = summ;
//         }

//         return max(maxx-minn, max(maxx, -minn));
//     }
// };


/*
Input: nums = [1,-3,2,3,-4]
Output: 5

1,-2,0,3,-1

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
2,-3,-2,-6,-3,-5


nums = [-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8]
output = 27

-3,-5, -3, -2, -6,  3,10,-10, -8, -3,  0, 10,  3, -5,  8, 7, -9, -9,  5, -8
-3,-8,-11,-13,-19,-16,-6,-16,-24,-27,-27,-17,-14,-19,-11,-4,-13,-22,-17,-25
*/