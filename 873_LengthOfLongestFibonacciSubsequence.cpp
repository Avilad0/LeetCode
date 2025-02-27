#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        unordered_map<int,int> valToIndex;
        int n = arr.size(), maxCount = 2;
        vector<vector<int>> dp(n, vector<int>(n,0));

        for (int curr=0; curr<n; ++curr){
            valToIndex[arr[curr]] = curr;
            for (int prev=0; prev<curr; ++prev){
                if ((arr[curr]-arr[prev] < arr[prev]) &&  valToIndex.find(arr[curr]-arr[prev])!=valToIndex.end()){
                    dp[prev][curr] = dp[valToIndex[arr[curr]-arr[prev]]][prev] + 1;
                } else {
                    dp[prev][curr] = 2;
                }

                if (dp[prev][curr]>maxCount)    maxCount = dp[prev][curr];
            }
        }

        return maxCount>2 ? maxCount : 0;
    }
};


// class Solution {
// public:
//     int lenLongestFibSubseq(vector<int>& arr) {
//         unordered_set<int> setArr(arr.begin(), arr.end());
//         int n = arr.size(), maxCount = 1;

//         for (int i=0;i<n;++i){
//             for ( int j=i+1; j<n;++j){
//                 int first = arr[i], second = arr[j], count =2, t;
//                 while (setArr.count(first+second)>0){
//                     count++;
//                     t = first;
//                     first = second;
//                     second += t;
//                 }

//                 if (count>maxCount) maxCount = count;
//             }
//         }

//         if (maxCount<3) return 0;
//         return maxCount;
//     }
// };