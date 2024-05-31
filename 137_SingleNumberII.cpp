#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int ans=0;

        int count,set_bit=1;
        for(int b=0; b<32 ;++b){
            count=0;
            for (int& num :nums){
                count+=((num & set_bit)==0?0:1);
            }

            if ((count%3)!=0){
                ans|=set_bit;
            }

            set_bit<<=1;
        }

        return ans;
    }
};

int main(){
    Solution s;
    vector<int> n = {-2,-2,1,1,4,1,4,4,-4,-2};
    cout<<s.singleNumber(n);
    return 0;
}


// Input: 
// nums = [2,2,3,2]
// xor    [2,0,3,1]
// and    [2,0,3,0]


// Output: 3

// Input: 
// nums = [0,1,0,1,0,1,5]
//        [0,1,1,0,0,1,4]
//        [0,1,0,0,0,1,4]

// Output: 99


// [4,2,4,2,4,2,5]
       