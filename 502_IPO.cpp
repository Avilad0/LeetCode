#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pi;

class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        priority_queue< pi, vector<pi>, greater<pi>> sortedPairs;
        int n = profits.size(),i;
        for (i=0;i<n;++i){
            sortedPairs.push({capital[i], profits[i]});
        }

        priority_queue<int> maxProfitQueue;
        i=0;
        while(k--){        
            for (;i<n && sortedPairs.top().first<=w; ++i){
                maxProfitQueue.push(sortedPairs.top().second);
                sortedPairs.pop();
            }

            if (maxProfitQueue.empty()){
                break;
            }

            w+=maxProfitQueue.top();
            maxProfitQueue.pop();
        }

        return w;
    }
};





        // int n = profits.size(),i;

        // int max_profit = 0, max_index=-1, _;
        // for (_=0;_<k;++_){
        //     for (i=0;i<n;i++){
        //         if (capital[i]<=w && profits[i]>max_profit){
        //             max_index=i;
        //             max_profit = profits[i];
        //         }
        //     }
        //     if (max_index==-1){
        //         break;
        //     } else{
        //         w+=max_profit;
        //         profits[max_index]=-1;
        //         max_profit = 0;
        //         max_index=-1;
        //     }
        // }

        // return w;