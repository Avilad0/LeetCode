#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        int n=candies.size(), ans=0, left=1, right=*max_element(candies.begin(), candies.end()), mid, i;
        long long count;     

        while(left<=right){
            mid= (left+right)/2;

            count=0;
            for (i=0; i<n; ++i){
                count+= (candies[i]/mid);
            }

            if (count>=k){
                ans=mid;
                left=mid+1;
            } else {
                right=mid-1;
            }
        }

        return ans;
    }
};