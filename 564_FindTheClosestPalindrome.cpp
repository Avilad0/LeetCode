#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string nearestPalindromic(string n) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        int len = n.size();
        bool isOdd = len%2==1;
        long half = stol(n.substr(0, isOdd?len/2+1:len/2)), oldInteger = stol(n), diff = LONG_MAX, ans, tempDiff;

        vector<long> allPalindromes;
        allPalindromes.push_back(createPalindrome(half, isOdd));
        allPalindromes.push_back(createPalindrome(half +1, isOdd));
        allPalindromes.push_back(createPalindrome(half -1, isOdd));
        allPalindromes.push_back(pow(10, len-1) -1);
        allPalindromes.push_back(pow(10, len) +1);

        for (auto& palindrome: allPalindromes){
            
            tempDiff = abs(palindrome-oldInteger);
            if (tempDiff==0) continue;

            if (diff > tempDiff){
                ans = palindrome;
                diff = tempDiff;
            } else if (tempDiff==diff){
                ans = min(ans, palindrome);
            }
        }

        return to_string(ans);
    }

private:

    long createPalindrome(long half, bool isOdd){
        long palindrome = half;
        if (isOdd) half/=10;

        while (half){
            palindrome = palindrome*10 + half%10;
            half/=10;
        }

        return palindrome;
    }

};

// class Solution {
// public:
//     string nearestPalindromic(string n) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
//         int s=n.size(), left, right;
//         originalInteger = stoi(n), newInteger=-1;

//         if (s%2==1){
//             left=right=s/2;
//         } else {
//             right = s/2;
//             left = s/2 -1;
//         }

//         findPalindrome(n, left, right);

//         if (newInteger==originalInteger){
//             if (n[left]=='0') {
//                 n[left]=n[right]='1';
//             } else {
//                 n[left]=n[right]=n[right]-1;
//             }
//             return n;
//         }

//         return to_string(newInteger);
//     }

// private:
//     long long originalInteger, newInteger;
//     void findPalindrome(string& n, int left, int right){
        
//         if (left==-1){
//             if (newInteger==-1 || abs(newInteger-originalInteger) > abs(stoi(n) - originalInteger)){
//                 newInteger = stoi(n);
//             }
//             return;
//         }

//         if (n[left]==n[right]){
//             findPalindrome(n, left-1, right+1);
//         } else {
//             char temp= n[left];
//             n[left]=n[right];
//             findPalindrome(n, left-1, right+1);
//             n[left]=temp;

//             temp = n[right];
//             n[right]=n[left];
//             findPalindrome(n, left-1, right+1);
//             n[right]=temp;
            
//         }
//     }

// };

int main(){
    Solution s;
    // cout<<s.nearestPalindromic("1213");
    // cout<<s.nearestPalindromic("1221");
    cout<<s.nearestPalindromic("1");
    return 0;
}



/*
n=101
o=99
others = 111


n=10
o=9
others = 11

n = 1213

o = 1221
others =
    1111
    3223
    3113



/////
n = 122341

for cost 3 :
o = 122221,
    133331,
    143341,


*/