#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthNumber(int n, int k) {
        long curr = 1;
        int newK = k, nextAtSameLevel=1;
        while (newK>1){
            int count = getNumsInSubtree(curr, n);
            if (count<newK){
                newK -= count;
                curr += 1;
            } else {
                curr*=10;
                newK-=1;
            }
        }

        return curr;
    }

private:
    int getNumsInSubtree(long curr, const int& n){
        long nxt = curr+1, count = 0;
        while (curr<=n){
            nxt = min(nxt, n+1l);
            count += nxt-curr;
            curr*=10;
            nxt*=10;
        }

        return count;
    }
};

int main(){
    Solution s;
    cout<<s.findKthNumber(13, 3);
    return 0;
}


/*
Input: n = 13, k = 2
Output: 10
[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

[1]*[-,0..3]
[2]*[-]
[3]*[-]
[4]*[-]
[5]*[-]
[6]*[-]
[7]*[-]
[8]*[-]
[9]*[-]


200
1*[-,0..9]*[-,0..9]

*/