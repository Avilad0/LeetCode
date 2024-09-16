#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);   

        set<int> setOfTimeInMinutes;
        int timeInMinutes;
        for (auto& time: timePoints){
            timeInMinutes = stoi(time.substr(0,2))*60 + stoi(time.substr(3,2));
            if ( setOfTimeInMinutes.find(timeInMinutes) != setOfTimeInMinutes.end()) return 0;

            setOfTimeInMinutes.insert(timeInMinutes);    
        }

        int minDiff = 1440 - *setOfTimeInMinutes.rbegin() + *setOfTimeInMinutes.begin();

        for (int i=1; i<setOfTimeInMinutes.size(); ++i){
            minDiff = min(minDiff, *next(setOfTimeInMinutes.begin(),i) - *next(setOfTimeInMinutes.begin(),i-1));
        }

        return minDiff;
    }
};



// Input: timePoints = ["23:59","00:00"]
// Output: 1

// Input: timePoints = ["00:00","23:59","00:00"]
// Output: 0
 
// 23:59 = 1439