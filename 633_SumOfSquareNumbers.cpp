#include<bits/stdc++.h>
using namespace std;

//with no extra space compared to below
class Solution {
public:
    bool judgeSquareSum(int c) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        unsigned int left=0, right = sqrt(c)+1, sum;

        while (left<=right){
            sum = left*left + right*right;

            if (sum == c){
                return true;
            } else if (sum>c) {
                --right;
            } else {
                ++left;
            }
        }

        return false;
    }
};


// class Solution {
// public:
//     bool judgeSquareSum(int c) {

//         if (c==0 || c==1 || c==2){
//             return true;
//         }
        
//         unordered_set<int> sqrs = {0,1};

//         unsigned int sqr,i;

//         for( i=2; (sqr= i*i) <=c;++i){
//             sqrs.insert(sqr);
//             if (sqrs.find(c-sqr)!= sqrs.end()){
//                 return true;
//             }
//         }
//         return false;
        
//     }
// };