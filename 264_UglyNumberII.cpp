#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        vector<int> uglyNumbers(n);
        uglyNumbers[0] = 1;

        int indexMultipleOf2 = 0, indexMultipleOf3 = 0, indexMultipleOf5 = 0;
        int nextMultipleOf2 = 2, nextMultipleOf3 = 3, nextMultipleOf5 = 5;

        for (int i = 1; i < n; i++) {
            int nextUglyNumber = min(nextMultipleOf2, min(nextMultipleOf3, nextMultipleOf5));
            uglyNumbers[i] = nextUglyNumber;

            if (nextUglyNumber == nextMultipleOf2) {
                indexMultipleOf2++;
                nextMultipleOf2 = uglyNumbers[indexMultipleOf2] * 2;
            }
            if (nextUglyNumber == nextMultipleOf3) {
                indexMultipleOf3++;
                nextMultipleOf3 = uglyNumbers[indexMultipleOf3] * 3;
            }
            if (nextUglyNumber == nextMultipleOf5) {
                indexMultipleOf5++;
                nextMultipleOf5 = uglyNumbers[indexMultipleOf5] * 5;
            }
        }

        return uglyNumbers[n - 1];
    }
};

// class Solution {
// public:
//     int nthUglyNumber(int n) {
//         long x;
//         set<long> unglyNumbers({1});

//         while (n){
//             x = *unglyNumbers.begin();
//             unglyNumbers.erase(unglyNumbers.begin());

//             unglyNumbers.insert(x*2);
//             unglyNumbers.insert(x*3);
//             unglyNumbers.insert(x*5);

//             --n;
//         }

//         return x;
//     }
// };


/*
2,3,5

[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

[1,2,3,5]
[1,2,3,4,5,6,10]
[1,2,3,4,5,6,8,9,10,12,15,20,25]


*/