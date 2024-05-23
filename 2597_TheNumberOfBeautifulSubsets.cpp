#include<bits/stdc++.h>
using namespace std;

class Solution {
    public:
        int beautifulSubsets(vector<int>& nums, int k) {
            map<int,map<int,int>> freq;
            for(int num:nums){
                freq[num%k][num]++;
            }

            int ans=1;
            for (auto& f1: freq){
                vector<pair<int,int>> subset(f1.second.begin(), f1.second.end());

                int n = subset.size();

                int curr=1,curr1=1;

                for(int i=n-1;i>=0; --i){
                    int skip = curr;
                    int take = (1<<subset[i].second) -1;

                    if ( i+1<n && subset[i+1].first-subset[i].first==k){
                        take*=curr1;
                    } else {
                        take*=curr;
                    }

                    curr1=curr;
                    curr = skip+take;
                }

                ans*=curr;
            }

            return ans-1;
        }
};


/*
#include<bits/stdc++.h>
using namespace std;

class Solution {
    public:
        int beautifulSubsets(vector<int>& nums, int k) {
            map<int,map<int,int>> freq;
            for(int num:nums){
                freq[num%k][num]++;
            }

            int ans=1;
            for (auto& f1: freq){
                vector<pair<int,int>> subset(f1.second.begin(), f1.second.end());

                int n = subset.size();

                vector<int> count(n+1);
                count[n]=1;

                for(int i=n-1;i>=0; --i){
                    int skip = count[i+1];
                    int take = (1<<subset[i].second) -1;

                    if ( i+1<n && subset[i+1].first-subset[i].first==k){
                        take*=count[i+2];
                    } else {
                        take*=count[i+1];
                    }

                    count[i] = skip+take;
                }

                ans*=count[0];
            }

            return ans-1;
        }
};
*/

/*
[2,3,9] = 4 + 3 + 1 = 8 -3 -1 
[2,6] = 1 + 2 + 1 


2,3,6,9  k=3
[2], [3], [6], [9], [2,3], [2,6], [2,9], [3,9], [2,3,9]
ans =9 
uncompatible pairs = 2
2**4 = 16-1 =15

2,4,6,8  k=2
[2], [4], [6], [8], [2,6], [2,8], [4,8]
ans =7 
uncompatible pairs = 3
2**4 = 16-1=15

2,4,6 k=2
ans=4
uncompatible pairs = 2
2**3=8-1=7
*/