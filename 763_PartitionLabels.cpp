#include<bits/stdc++.h>
using namespace std;

// same complexity but more intuitive way of writing.
class Solution {
public:
    vector<int> partitionLabels(string s) {
        
        int n=s.size();
        
        vector<int> lastPos(26, -1), partitionSizes; 
        for (int i=0;i<n; ++i){
            lastPos[s[i]-'a'] = i;
        }

        int start, end, i=0;
        while (i<n){
            start = i;
            end = lastPos[s[i]-'a'];
            
            for(; i<=end; ++i){
                end = max(end, lastPos[s[i] - 'a']);
            }

            partitionSizes.emplace_back(end - start + 1);
        }


        return partitionSizes;
    }
};

// class Solution {
// public:
//     vector<int> partitionLabels(string s) {
        
//         int n=s.size(), i;
        
//         vector<int> lastPos(26, -1), partitionSizes; 
//         for (i=0;i<n; ++i){
//             lastPos[s[i]-'a'] = i;
//         }

//         int lastEnd = -1, end = -1;
//         for (i=0;i<n;++i){
//             if (end == lastEnd){
//                 end = lastPos[s[i]-'a'];
//             } else {
//                 end = max(end, lastPos[s[i]-'a']);
//             }

//             if (i==end){
//                 partitionSizes.emplace_back(end-lastEnd);
//                 lastEnd = end;
//             }
//         }

//         return partitionSizes;
//     }
// };

/*
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
The partition is "ababcbaca", "defegde", "hijhklij".

a b a b c b a c a d  e  f  e  g  d  e  h  i  j  h  k  l  i  j
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23

a : [0, 8]
b : [1, 5]
c : [4, 7]
d : [9, 14]
e : [10, 15]
f : [11, 11]
g : [13, 13]
h : [16, 19]
i : [17, 22]
j : [18, 23]
k : [20, 20]
l : [21, 21]

*/