#include<bits/stdc++.h>
using namespace std;

// 1-pass and O(1) space
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {

        int n=arr.size(), count =0, prefixSum = 0, mod = 1e9 + 7;
        vector<int> modCount = {1,0};

        for (int i=0;i<n;++i){
            prefixSum += arr[i];
            count = (count + modCount[(prefixSum+1)%2])%mod;
            modCount[prefixSum%2]++;
        }
        return count;
    }
};


// // 2-pass and O(N) space
// class Solution {
// public:
//     int numOfSubarrays(vector<int>& arr) {
//         int n=arr.size(), i=1, count =0;
//         vector<int> prefix(n+1,0), modCount(2,0);
//         for (; i<=n; ++i)    {
//             prefix[i] = prefix[i-1]+ arr[i-1];
//             modCount[prefix[i]%2] ++;
//         }

//         for (i=1;i<=n;++i){
//             count= ((long)count + modCount[(prefix[i-1] +1)%2]) % 1000000007;
//             modCount[prefix[i]%2]--;
//         }
//         return count;
//     }
// };


/*
Input: arr = [2,4,6]
Output: 0

2,6,12
startI=0, odds = 0 , evens = 3, count = 0
startI=1, odds = 0 , evens = 2, count = 0 + 0
startI=0, odds = 0 , evens = 3, count = 0 + 0 + 0

----
Input: arr = [1,2,3,4,5,6,7]
Output: 16

1,3,6,10,15,21,28

startI=0, odds = 4, evens = 3, count = 4  [1][1,2][1,2,3,4,5][1,2,3,4,5,6]
startI=1, odds = 3, evens = 3, count = 4 + 3 [2,3][2,3,4][2,3,4,5,6,7]
startI=2, odds = 2, evens = 3, count = 4 + 3 + 3 [3][3,4][3,4,5,6,7]
startI=3, odds = 2, evens = 2, count = 4 + 3 + 3 + 2 
startI=4, odds = 2, evens = 1, count = 4 + 3 + 3 + 2 + 2
startI=5, odds = 1, evens = 1, count = 4 + 3 + 3 + 2 + 2 + 1
startI=6, odds = 0, evens = 1, count = 4 + 3 + 3 + 2 + 2 + 1 + 1

ans = 16
*/