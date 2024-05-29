#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numSteps(string s) {
        
        int n = s.length();

        int ans = 0, carry =0;
        for(int i=n-1;i>0;--i){
            if((int(s[i]) + carry)%2==0){
                ++ans;
            }else{
                ans+=2;
                carry=1;
            }
        }

        return ans + carry;
    }
};


// 101110001111
// 101110010000
// 10111001
// 1011101
// 101111
// 11
// 1


// 1+ 4 + 1 + 1 + 1+1 + 1+ 4 + 1 + 2 = 17 


//1101
//6

//10
//1


// 10000