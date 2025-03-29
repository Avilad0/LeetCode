#include<bits/stdc++.h>
using namespace std;

// m = max number in nums
// TC = O(nlog(n) + n*Sqrt(m) + n + log(totalExponents=numberOfOperations)) = O(nlog(n) + n*Sqrt(m) + n + log(k))
//    = O(n * (log(n)+sqrt(m)) )
// SC = O(5n) = O(n)

//monotonic stack + priority queue + binary exponentiation
// [can even use sieve of Eratosthenes for finding the prime factors.]
class Solution {

private:
    const int MOD = 1e9 + 7;
    long long power(long long base, long long exponent) {
        long long res = 1;

        while (exponent > 0) {
            if (exponent % 2 == 1) {
                res = ((res * base) % MOD);
            }

            base = (base * base) % MOD;
            exponent /= 2;
        }

        return res;
    }
    
public:
    int maximumScore(vector<int>& nums, int k) {
        int n = nums.size(), uniquePrimes;
        priority_queue<pair<int,int>> maxHeap;
        
        vector<int> primeScores;
        for (int i=0;i<n; ++i){
            maxHeap.emplace(nums[i], i);
            uniquePrimes = 0;
            int factor = 2, num = nums[i];
            for (; factor<=sqrt(num) && num >1; factor++){
                if (num%factor==0){
                    ++uniquePrimes;   
                    while (num%factor==0)   num/=factor;
                }
            }
            if (num>1) uniquePrimes++; //remaining num is a prime number

            primeScores.emplace_back(uniquePrimes);
        }

        vector<int> nextDominant(n,n), prevDominant(n,-1);
        stack<int> decreasingPrimeScores;

        for (int i=0; i<n; ++i){
            while (!decreasingPrimeScores.empty() && primeScores[decreasingPrimeScores.top()]<primeScores[i]){
                nextDominant[decreasingPrimeScores.top()] = i;
                decreasingPrimeScores.pop();
            }

            if (!decreasingPrimeScores.empty()) prevDominant[i] = decreasingPrimeScores.top();
            
            decreasingPrimeScores.emplace(i);
        }

        int score =1;
        while (k>0 && !maxHeap.empty()){
            auto [curr, index] = maxHeap.top();
            maxHeap.pop();

            long long numOfSubArrays = (long long)(nextDominant[index]-index)*(index - prevDominant[index]);
            long long operations = min(numOfSubArrays, (long long) k);
            score = (score * power(curr, operations))%MOD;
            k-=operations;
        }
        
        return score;
        
    }
};

int main(){
    Solution s;
    // vector<int> nums = {8,3,9,3,8}; 
    // int k = 2;
    // cout<<s.maximumScore(nums, k);

    vector<int> nums = {3289,2832,14858,22011}; 
    int k = 6;
    cout<<s.maximumScore(nums, k); //
    return 0;
}
