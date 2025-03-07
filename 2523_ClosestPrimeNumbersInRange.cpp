#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> closestPrimes(int left, int right) {
        vector<bool> isPrime(right+1, true);
        isPrime[1]=false;
        int i,j;
        for (i=2;i*i<=right; ++i){
            if (isPrime[i]){
                for (j=i+i; j<=right; j+=i){
                    isPrime[j]=false;
                }
            }
        }


        int minDistance = INT_MAX, lastPrime=-1;
        vector<int> ans = {-1,-1};
        for (i=left; i<=right; ++i){
            if (isPrime[i]){
                if (lastPrime!=-1 && i-lastPrime<minDistance){
                    minDistance = i-lastPrime;
                    ans[0]=lastPrime;
                    ans[1]=i;
                }
                lastPrime=i;
            }
        }

        return ans;
    }
};