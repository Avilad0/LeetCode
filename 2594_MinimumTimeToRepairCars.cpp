#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long ans=0, left=0, right= ((long long)*min_element(ranks.begin(), ranks.end()))*cars*cars, mid;
        int remainingCars, n=ranks.size(), i;
        
        while (left<=right){
            mid = left + (right-left)/2;
            
            remainingCars = cars;
            for (i=0; i<n && remainingCars>0; ++i){
                remainingCars -= (int) sqrt(mid/ranks[i]);
            }

            if (remainingCars <= 0){
                ans = mid;
                right = mid-1;
            } else {
                left = mid+1;
            }
        }

        return ans;
    }
};

int main(){
    Solution s;
    vector<int> ranks = {4,2,3,1};  int cars = 10;  //16
    cout << s.repairCars(ranks, cars) << endl;
    return 0;
}