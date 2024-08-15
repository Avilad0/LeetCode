#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        int fives=0, tens=0, twentys=0;
        for (auto& b: bills){
            if (b==5){
                ++fives;
            } else if(b==10){
                if (fives==0) {
                    return false;
                }
                --fives;
                ++tens;
            } else { //b==20
                if (tens>0 && fives>0){
                    --tens;
                    --fives;
                    ++twentys;
                } else if ( fives>=3){
                    fives-=3;
                    ++twentys;
                } else{
                    return false;
                }
            }
        }

        return true;
    }
};