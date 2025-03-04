#include<bits/stdc++.h>
using namespace std;

//try to represent it in a number of base 3 (like 1*3(2) + 0*3(1) + 2*3(0))
// if any power needs to be multiplied by 2, then no possibility of distinct powers.
// tc = O(log3(n)), sc = O(1)
class Solution {
public:
    bool checkPowersOfThree(int n) {
        int i=0;
        while (n>0){
            if (n%3==2) return false;
            
            n/=3; //integer floor value
        }

        return true;
    }
};

// tc = O(2^(Log3(n)), sc = O(log3(n))
// class Solution {
// private:
//     bool helper(int n, int nextpower){
//         int y = pow(3,nextpower);
//         if (y==n)  return true;
//         if (y>n)   return false;
        
//         return helper(n-y, nextpower+1) || helper(n, nextpower+1);
//     }

// public:
//     bool checkPowersOfThree(int n) {
//         return helper(n, 0);
//     }
// };