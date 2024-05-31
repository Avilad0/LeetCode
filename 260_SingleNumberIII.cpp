#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        
        long nums_xor=0;
        for (int& num:nums) 
            nums_xor^=num;

        // int set_bit=1;
        // while((set_bit & nums_xor)==0){
        //     set_bit<<=1;
        // }

        //above commented can be done in constant time as  below.
        // xor-1 will flip the minimum set bit and &xor will remove the other changed bits if any, and ^xor will turn all set bits to zero except the flipped bit.
        //( 5 & (5-1))^5 = 1
        int set_bit= (nums_xor & (nums_xor-1)) ^ nums_xor;


        int xor1=0, xor2=0;
        for (int& num:nums){
            if ((set_bit & num)==0){
                xor1^=num;
            } else{
                xor2^=num;
            }
        }

        return {xor1,xor2};
    }
};

int main(){
    Solution s;
    vector<int> nums = {1,2,1,3,2,5};
    for(int& num:s.singleNumber(nums)) cout<<num<<" ";
    return 0;
}