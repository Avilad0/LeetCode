#include<bits/stdc++.h>
using namespace std;

// same complexity as below, but 1 pass instead of 2-pass
// calculate number of substrings ending at index, based on the min position of a,b,c. 
// So substring ending at index, will be any string formed by adding chars before the min position of a,b,c
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n=s.size(), ans=0;        
        vector<int> pos(3,-1);
        for (int index=0;index<n;index++){
            pos[s[index]-'a'] = index;
            ans += 1+ (min({pos[0],pos[1],pos[2]}));
        }

        return ans;
    }
};

// // same as below, but little simplified
// class Solution {
// public:
//     int numberOfSubstrings(string s) {
//         int n=s.size(), slow=0, fast=0, ans=0;        
//         vector<int> count(3,0);
//         for (;fast<n;fast++){
//             count[s[fast]-'a']++;
//             while (count[0]>0 && count[1]>0 && count[2]>0){
//                 ans += (n-fast);
//                 count[s[slow]-'a']--;
//                 slow++;
//             }
//         }

//         return ans;
//     }
// };
    

// class Solution {
// public:
//     int numberOfSubstrings(string s) {
//         int n=s.size(), slow=0, fast=0, ans=0, lastMatchIndex=-1;        
//         vector<int> count(3,0);
//         for (;fast<n;fast++){
//             count[s[fast]-'a']++;
//             if (count[0]>0 && count[1]>0 && count[2]>0){
//                 lastMatchIndex = slow;
//                 while (count[0]>0 && count[1]>0 && count[2]>0){
//                     count[s[slow]-'a']--;
//                     slow++;
//                 }
//                 ans += ((slow-lastMatchIndex)*(n-fast));
//             }
//         }

//         return ans;
//     }
// };

int main(){
    Solution sol;
    cout<<sol.numberOfSubstrings("abcabc")<<endl; //10
    return 0;
}