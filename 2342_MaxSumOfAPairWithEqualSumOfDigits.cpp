#include<bits/stdc++.h>
using namespace std;

/*
    space complexity can be decresed to log10(largestNumber) by using array int[82]
    sum of digits is 0 to 81 for numbers from 0 to 10**9
*/

class Solution {
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int,int> sums;
        int maxSum= -1, currentSum, t;

        for (int num: nums){
            currentSum = 0;
            t = num;
            while (t!=0){
                currentSum += (t%10);
                t/=10;
            }
            if (sums.find(currentSum)!=sums.end()){
                if (maxSum < (sums[currentSum] + num) ){
                    maxSum = sums[currentSum] + num;
                }
                if (sums[currentSum] < num){
                    sums[currentSum] = num;                        
                }
            } else {
                sums[currentSum] = num;
            }
        }

        return maxSum;
    }
};