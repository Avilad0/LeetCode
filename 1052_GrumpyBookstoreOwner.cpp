#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(NULL);
        int n=customers.size(), maxSatisfied = 0, i, runningSatisfied,ans=0;
        for (i=0;i<minutes;++i){
            if (grumpy[i]==1){
                maxSatisfied += customers[i];
            } else {
                ans += customers[i];
            }
        }

        runningSatisfied = maxSatisfied;
        for (;i<n;++i){
            if (grumpy[i-minutes]==1){
                runningSatisfied-=customers[i-minutes];
            }

            if (grumpy[i]==1){
                runningSatisfied+=customers[i];
                if (runningSatisfied>maxSatisfied){
                    maxSatisfied=runningSatisfied;
                }
            } else{
                ans+=customers[i];
            }
        }
        return ans + maxSatisfied;
    }
};

int main(){
    Solution s;
    vector<int> customers = {1,0,1,2,1,1,7,5}, grumpy = {0,1,0,1,0,1,0,1};
    int minutes = 3;
    cout<<s.maxSatisfied(customers,grumpy, minutes);
    return 0;
}