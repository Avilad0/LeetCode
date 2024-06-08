#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        if (n<2){
            return false;
        }

        unsigned int sum=0;

        unordered_map<int,int> remainders;
        remainders[0]=-1;

        int i,t;
        for (i=0;i<n;++i){
            sum+=nums[i];
            t=sum%k;
                        
            if (remainders.find(t)!=remainders.end()){
                if (i-remainders[t]>1){
                    return true;
                }
            } else{
                remainders[t]=i;
            }
        }
        return false;
    }
};

int main(){
    Solution s;
    // vector<int> nums = {1,2,3};
    // int k = 5;
    vector<int> nums = {23,2,4,6,6};
    int k = 7;
    cout<<s.checkSubarraySum(nums, k);
    return 0;
}
 


// k = 9
        
// nums = 1 2 3  5  5  6  7  8  9
// sum  = 1 3 6 11 16 22 29 37 46
// %    = 1 3 6  2  7  4  2  1  1




// nums = [23,  2,  6,  4,  7], k = 6
// sum  = [23, 25, 31, 35, 42]
// %    = [ 5,  1,  1,  5,  0]
