#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxDistance(vector<int>& position, int m) {

        sort(position.begin(), position.end());
        int n = position.size(),i,counter;
        long ans=0,left = 1, right = ((position[n-1]-position[0])/(m-1)) +1,range,prev;
        
        while (left<=right){
            prev=position[0];
            counter=1;
            range=(left+right)/2;
            for (i=1;i<n;++i){
                if (position[i]-prev>=range){
                    prev =position[i];
                    ++counter;
                }
            }
            if (counter>=m){
                ans=range;
                left = range + 1;
            } else{
                right = range-1;
            }
        }

        return ans;
        
    }
};

int main(){
    Solution s;
    // vector<int> position = {1,2,3,4,7};
    // int m = 3;
    vector<int> position = {1,2,3,4,5,6,7,8,9,10};
    int m = 4;

    // vector<int> position = {5,4,3,2,1,1000000000};
    // int m = 2;
    cout<<s.maxDistance(position, m);
    return 0;
}


// Input: position = [1,2,3,4,7], m = 3
// Output: 3          -     - -
//                    [1,1,1,3]

// Input: position = [1,2,3,4,7], m = 4
//                    - -   - -
//                    [1,1,1,3]
// Output: 1


// [1,2,3,4,5,6,7,8,9,10,11,12] ,  m=5
//  -     -     -      -     -
//  ans: 2


// [1,2,4,5,8,9,10,13] ,  m=5
//  -     - -    -  -
//  -   -   -    -  -
//  [1,2,1,3,1,1, 3]
//  ans: 2


// [1,5,8,10,13] ,  m=5
//  - - -  -  -
//  [4,3,2, 3]
//  ans: 2

 