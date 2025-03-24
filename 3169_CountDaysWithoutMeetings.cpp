#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        
        meetings.push_back({0, 0});
        meetings.push_back({days+1, days+1});
        sort(meetings.begin(), meetings.end(),  [](const vector<int>& a, const vector<int>& b){
                                                    return a[0] < b[0];
                                                });
        
        int count =0, m = meetings.size(), curr=1, prev =0;
        
        while (curr<m){
            if (meetings[prev][1] >= meetings[curr][1]){
                curr++;
            } else {
                if (meetings[curr][0] > meetings[prev][1]+1){
                    count += (meetings[curr][0] - meetings[prev][1] -1);
                }
                prev = curr++;
            }
        }

        return count;
    }
};



// // Memory Limit Exceeded for days = 1e9
// // can be solved by using a priority queue with only meeting to perform linesweep. Similar to above
// class Solution {
// public:
//     int countDays(int days, vector<vector<int>>& meetings) {
//         vector<int> lineSweep(days+2, 0);
//         for (auto& meeting: meetings){
//             lineSweep[meeting[0]]++;
//             lineSweep[meeting[1]+1]--;
//         }        

//         int count = 0;
//         for (int i=1 ;i<=days; ++i){
//             lineSweep[i] += lineSweep[i-1];
//             if (lineSweep[i] == 0){
//                 count++;
//             }
//         }

//         return count;
//     }
// };