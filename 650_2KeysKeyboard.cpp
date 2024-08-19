#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minSteps(int n) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int ans = 0, div=2;
        while (n!=1) {
            while (n%div==0){
                ans+=div;
                n/=div;
            }
            ++div;
        }

        return ans;       
    }
};



/*
n=3, ans=3  [CPP]
A
AA
AAA

n=5, ans=5, [CPPPP]
A
AA
AAA
AAAA
AAAAA

n=9, ans=6 [CPPCPP]
A
AA
AAA
AAAAAA
AAAAAAAAA


n=12, ans=7  [CPCPCPP]
A
AA
AAAA
AAAAAAAA
AAAAAAAAAAAA
*/