#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countTriplets(vector<int>& arr) {
        int ans = 0, running_xor = 0, i;
        map<int,pair<int,int>> xor_position_sums_and_counts={{0,{0,1}}}; //key:xor, first: sum, second: count
        

        for (i=0; i<arr.size(); ++i){
            running_xor^=arr[i];

            ans += ((xor_position_sums_and_counts[running_xor].second++ * i) - xor_position_sums_and_counts[running_xor].first);

            xor_position_sums_and_counts[running_xor].first+=i+1;

        }

        return ans;
    }
};


//inner for loop can be converted to formula as stated above
// prev_counts_of_xor*current_index - prev_sum_of_xor
// for subtracting the 1, we can add 1 to each index while adding it to prev_sum_of_xor to account for the -1;

//instead of the xor_indexes[0].push_back(-1);, we will have xor_p.. arr with starting value 0:{-1+1, 1} = 0:{0,1}




    // int countTriplets(vector<int>& arr) {
    //     int ans = 0, running_xor = 0,i,j;
    //     map<int,vector<int>> xor_indexes;
    //     xor_indexes[0].push_back(-1);

    //     for (i=0; i<arr.size(); ++i){
    //         running_xor^=arr[i];
    //         xor_indexes[running_xor].push_back(i);

    //         for (j =0;j<xor_indexes[running_xor].size()-1;++j){
    //             ans+= i-xor_indexes[running_xor][j]-1;
    //         }
    //     }

    //     return ans;
    // }


// Input: arr = [2,3,1,6,7]
// Output: 4
// Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

// xor =  [2, 1, 0, 6, 1]
//         0, 1, 2, 3, 4
//         -  -  - 
//         -     -
//               -  -  -
//               -     -

// 0:[-1,2] : 2 - -1 -1 = 2
// 1:[1,4]  : 4- 1 -1 =2


// Input: arr = [1,1,1,1,1]
// xor =        [1,0,1,0,1]
//               - -
//               - -   -
//               -   - -
//               -     -
//                 - -
//                 - -   -
//                 -   - -
//                 -     -
//                   - -
//                     - -
// 0:[-1,1,3]

// -1->1 : 1 - -1 -1 = 1
// -1->3 : 3 - -1 -1 = 3
// 1->3  : 3-1-1= 1 

// 1:[0,2,4]
// 0->2 : 2-0-1 = 1
// 0->4 : 4-0-1 = 3
// 2->4 : 4-2-1 = 1

// Output: 10


// in = [2, 4, 2, 1, 5, 7, 4]
// xor =[2, 6, 4, 5, 0, 7, 3]

