#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int> pi;

class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        int n = profit.size(), m = worker.size(),i, j;
        
        priority_queue<pi> maxProfitQueue;
        for (i=0;i<n;++i){
            maxProfitQueue.push({profit[i],difficulty[i]});
        }

        sort(worker.begin(), worker.end());
        i=m-1;
        unsigned long ans = 0;
        pi t;
        while (i>=0 && !maxProfitQueue.empty()){
            t = maxProfitQueue.top();
            maxProfitQueue.pop();
            j=0;
            while (i>=0 && worker[i]>=t.second){
                --i;
                ++j;
            }
            ans= ans + j*t.first;
        }
        return ans;
    }
};

int main(){
    vector<int> difficulty = {5,9,16,20,34,38,38,49,75,82},
        profit = {18,19,20,22,29,31,48,58,67,82},
        worker = {37,20,8,20,17,65,86,76,44,91};

    // vector<int> difficulty  = { 2, 4, 6, 8,10},
    //             profit      = {10,20,30,40,50},
    //             worker = {4,5,6,7};
    Solution s;
    cout<<s.maxProfitAssignment(difficulty,profit,worker);
    return 0;
}


// t.second =  20
// worker   =  10  15  19 20  21   25
//                                 i
//                             i
//                         i


// t.second =  20
// worker   =  10  15  19  21   25
//                              i
//                         i
//                     i
//                         i


// difficulty = { 5, 9, 16,  20,       34,   38,    38,49,75,   82},
//     profit = {18,19, 20,  22,       29,   31,    48,58,67,   82},
//     worker = { 8,    17,  20,20,    37,          44,65,76,   86,91};

// ans  = 82*2 + 67 + 58 + 48 + 29 + 22*2 + 20 + 18 = 448