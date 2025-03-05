#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long coloredCells(int n) {
        return ((long long) n*(n-1)*2) + 1;
    }
};

// class Solution {
// public:
//     long long coloredCells(int n) {
//         if (n==1) return 1;

//         long long ans = 0;
//         for (int i=0;i<n-1;i++) ans+= (i*4 + 2);

//         return ans + ((n-1)*2 + 1);
//     }
// };


/*
1->5->13->25->
1 +4  +8 +12 +16
1 +4(1+2+3+4+....n-1)
return (long long) (n*(n-1)/2)*4 + 1
*/