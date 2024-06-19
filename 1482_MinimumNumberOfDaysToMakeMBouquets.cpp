#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        int n = bloomDay.size();
        if (n< ((long long) m*k)){
            return -1;
        }

        int left=bloomDay[0], right=bloomDay[0], mid, running_m, counter, i,ans;

        for (i=1; i<n; ++i){
            if (bloomDay[i]<left)   left = bloomDay[i];
            if (bloomDay[i]>right)  right = bloomDay[i];
        }

        while(left<=right){
            mid = (left+right)/2;
            running_m=0;
            counter=0;
            for(i=0;i<n;++i){
                if (bloomDay[i]<=mid){
                    counter++;
                    if (counter==k){
                        running_m++;
                        counter=0;
                    }
                } else {
                    counter=0;
                }
            }

            if(running_m>=m){
                right = mid-1;
                ans = mid;
            } else {
                left = mid+1;
            }
        }

        return ans;

    }
};

// class Solution {
// public:
//     int minDays(vector<int>& bloomDay, int m, int k) {
        
//         int n = bloomDay.size();
//         if (n< ((long long) m*k)){
//             return -1;
//         }

//         set<int> sortedBloomDaySet(bloomDay.begin(), bloomDay.end());
//         vector<int> sortedBloomDay(sortedBloomDaySet.begin(), sortedBloomDaySet.end());

//         int left=0, right=sortedBloomDay.size()-1, mid, sortedMidValue, running_m, counter, i, isZeroPresent,ans=-1;

//         while(left<=right){
//             mid = (left+right)/2;
//             sortedMidValue = sortedBloomDay[mid];
//             running_m=0;
//             counter=0;
//             isZeroPresent=false;
//             for(i=0;i<n;++i){
//                 if (bloomDay[i]<sortedMidValue){
//                     counter++;
//                 } else if (bloomDay[i]==sortedMidValue){
//                     counter++;
//                     isZeroPresent=true;
//                 } else {
//                     counter=0;
//                 }

//                 if (counter==k){
//                     running_m++;
//                     counter=0;
//                 }
//             }

//             if(running_m>=m){
//             //     return sortedMidValue;
//             // } else if (running_m>m ){
//             //                 // } else if ( (running_m==m && !isZeroPresent) || running_m>m ){

//                 right = mid-1;
//                 ans = sortedMidValue;
//             } else {
//                 left = mid+1;
//             }
        
//         }

//         return ans;

//     }
// };



    // int minDays(vector<int>& bloomDay, int m, int k) {
        
    //     int n = bloomDay.size();
    //     if (n< ((long long) m*k)){
    //         return -1;
    //     }


    //     int left=*min_element(bloomDay.begin(), bloomDay.end()), right=*max_element(bloomDay.begin(), bloomDay.end()), mid, running_m, counter, i,ans=-1;

    //     while(left<=right){
    //         mid = (left+right)/2;
    //         running_m=0;
    //         counter=0;
    //         for(i=0;i<n;++i){
    //             if (bloomDay[i]<=mid){
    //                 counter++;
    //                 if (counter==k){
    //                     running_m++;
    //                     counter=0;
    //                 }
    //             } else {
    //                 counter=0;
    //             }

    //         }

    //         if(running_m>=m){
    //             right = mid-1;
    //             ans = mid;
    //         } else {
    //             left = mid+1;
    //         }
        
    //     }

    //     return ans;

    // }


int main(){
    Solution s;
    vector<int> bloomDay = {7,7,7,7,12,7,7};
    int  m = 2, k = 3;

    // vector<int> bloomDay = {1,2,4,9,3,4,1};
    // int  m = 2, k = 2;
    cout<<s.minDays(bloomDay, m, k);
    return 0;
}


// bloomDay = [1,2,4,9,3,4,1] m = 2 k = 2

// [1,2,3,4,9]
//  l   m   r
//        l r
//        m

        



        // int minimum, counter, running_m,i;
        // while (m){
        //     minimum = *min_element(bloomDay.begin(), bloomDay.end());
        //     counter=0;
        //     running_m=0;
        //     for (i=0;i<n;++i){
        //         if (bloomDay[i]-minimum<1){
        //             ++counter;
        //             if (counter==k){

        //             }
        //         }else{
        //             counter=0;
        //         }
        //     }

        // }

// bloomDay = [ 7, 7, 7, 7,12, 7, 7], m = 2, k = 3
