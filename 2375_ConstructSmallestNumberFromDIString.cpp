#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string smallestNumber(string pattern) {
        int n = pattern.size(), i=0,j, num = 1, countD=0;
        string ans(n+1,'0');
        for(i=0; i<=n; ++i){
            if (i==n || pattern[i]=='I'){
                if (countD>0){
                    j=i;
                    while(i-j<=countD)    
                        ans[j--] = char(48 + num++);
                    countD=0;
                } else {
                    ans[i] = char(48 + num++);
                }

            } else {
                countD++;
            }
        }
        return ans;
    }
};

// class Solution {
// public:
//     string smallestNumber(string pattern) {
//         int n = pattern.size(), i=0,j,count, num = 1, t;
//         string ans(n+1,'0');
//         while(i<=n){
//             j=i+1;
//             while(j<n && pattern[j]==pattern[i])
//                 ++j;

//             if (i==n || pattern[i]=='I'){
//                 while(i<j || i==n)  
//                     ans[i++] = char(48 + num++);
//             } else {
//                 t = j+1;
//                 while(i<=j)  
//                     ans[j--] = char(48 + num++);
//                 i=t;
//             }
//         }
//         return ans;
//     }
// };

int main(){
    Solution s;
    cout<<s.smallestNumber("DDIIDI")<<"\n"; //3214657
    cout<<s.smallestNumber("DDD")<<"\n"; //4321
    cout<<s.smallestNumber("IIIDIDDD")<<"\n"; //123549876
    cout<<s.smallestNumber("III")<<"\n"; //1234
    cout<<s.smallestNumber("DDIIDDID")<<"\n"; //321476598

    return 0;
}


/*
III
1234

IIIDIDDD
123
12354
12354
123549876

DDD
4321

DDIIDDID
321
3214
3214765
3214765
321476598

DDIIDI
321
3214
321465
3214657

*/