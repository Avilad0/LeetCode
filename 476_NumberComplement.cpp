#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findComplement(int num) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        return (1l<<(int(log2(num)) +1)) -1- num;
    }
};

// class Solution {
// public:
//     int findComplement(int num) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         long i=1;
//         while ( i <= num) i<<=1;

//         return i - 1 -num;
//     }
// };

int main(){
    Solution s;
    cout<<s.findComplement(5);
    return 0;
}