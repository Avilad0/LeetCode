#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {

        int n = hand.size();
        if (groupSize==1 || n==1){
            return true;
        }

        if (n%groupSize!=0){
            return false;
        }

        sort(hand.begin(), hand.end());

        int i=0, prev=hand[0], counter,curr;
        vector<pair<int,int>> freq;
        while(i<n){
            curr = hand[i];
            counter =1;

            while (i+1<n && hand[i+1]==curr){
                ++counter;
                ++i;
            }

            freq.push_back({curr, counter});
            ++i;
        }

        i=0;
        int len_freq = freq.size(),j, running_count;
        while (i<=len_freq-groupSize){
            running_count = freq[i].second;
            freq[i].second=0;
            for(j=1;j<groupSize;++j){
                freq[i+j].second-=running_count;
                if (freq[i+j].second<0 || freq[i+j-1].first!=freq[i+j].first-1){
                    return false;
                }
            }

            while(i<len_freq && freq[i].second==0){
                i++;
            }

        }

        return i==len_freq;
    }
};


int main(){
    Solution s;
    vector<int> hand = {1,2,3,6,2,3,4,7,8};
    cout<<s.isNStraightHand(hand, 3);
    return 0;
}        


        // int i=1, freq_count=1, prev=hand[0], group_counter=0;
        // while(i<n){
            


        //     while(i<n && hand[i]==hand[i-1]){
        //         ++freq_count;
        //         ++i;
        //     }

        //     if (hand[i]-1!=prev){
        //         return false;
        //     }

        //     group_counter = (group_counter+1)%3;



        //     freq_count=0;
        //     ++i;
        // }

// input :  5,6,6,6,7,7,7,7,8,8,8,9,9,10,11 groupsize=3
            // 1,    2,      3

// input :  5,6,6,7,7,7,7,8,8,8,9,9 groupsize=3



