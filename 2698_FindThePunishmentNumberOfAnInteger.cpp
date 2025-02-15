#include<bits/stdc++.h>
using namespace std;

class Solution {
    public:
    int punishmentNumber(int n) {
        int sums = 0, i=1;
        for(; i<=n; ++i)
            if (isPunishment(i,i*i,0)) sums+= (i*i);

        return sums;
    }

    private:
    bool isPunishment(int num, int square, int runningSum){
        if (square+ runningSum == num) return true;
 
        if (square == 0 )
            if (runningSum==num) return true;
            else return false;

        int z = 0, multiplier = 1;
        while (square){
            z = (square%10)*multiplier + z;
            square/=10;
            multiplier*=10;
            if (isPunishment(num,square,runningSum+z)){
                return true;
            }
        }

        return false;
    }
};


int main(){
    Solution s;
    cout<<s.punishmentNumber(10);
    return 0;
}