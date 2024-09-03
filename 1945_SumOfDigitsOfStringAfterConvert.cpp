#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int getLucky(string s, int k) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int number = 0,t;
        for (auto& c: s) {
            t= int(c-96);
            while(t){
                number+=(t%10);
                t/=10;
            }
        }


        while (--k){
            t=0;
            while(number){
                t+=(number%10);
                number/=10;
            }
            
            number=t;
            if (number<10) break;
        }

        return number;
    }
};

int main(){
    Solution soln;
    cout<<soln.getLucky("leetcode",2);
    return 0;
}