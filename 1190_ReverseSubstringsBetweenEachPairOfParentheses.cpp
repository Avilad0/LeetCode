#include<bits/stdc++.h>
using namespace std;

// O(n^2)
class Solution {
public:
    string reverseParentheses(string s) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        string t;
        int i,j;

        for (i=0;i<s.length(); ++i){

            if (s[i] == ')'){

                t = "";
                j=i-1;
                while (s[j] != '('){
                    t+=s[j];
                    --j;
                }

                s.replace(j, i-j + 1 ,t);
                i-=2;
            }
        }

        return s;

    }
};

// // O(n)
// class Solution {
// public:
//     string reverseParentheses(string s) {
//         int n = s.length();
//         stack<int> openParenthesesIndices;
//         vector<int> pair(n);

//         // First pass: Pair up parentheses
//         for (int i = 0; i < n; ++i) {
//             if (s[i] == '(') {
//                 openParenthesesIndices.push(i);
//             }
//             if (s[i] == ')') {
//                 int j = openParenthesesIndices.top();
//                 openParenthesesIndices.pop();
//                 pair[i] = j;
//                 pair[j] = i;
//             }
//         }

//         // Second pass: Build the result string
//         string result;
//         for (int currIndex = 0, direction = 1; currIndex < n;
//              currIndex += direction) {
//             if (s[currIndex] == '(' || s[currIndex] == ')') {
//                 currIndex = pair[currIndex];
//                 direction = -direction;
//             } else {
//                 result += s[currIndex];
//             }
//         }
//         return result;
//     }
// };




// O(n^2)
// class Solution {
// public:
//     string reverseParentheses(string s) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

//         stack<char> charStack; 
//         string t;

//         for (auto& c: s){

//             charStack.push(c);

//             if (c == ')'){
//                 charStack.pop();
//                 t = "";

//                 while (charStack.top() != '('){
//                     t+=charStack.top();
//                     charStack.pop();
//                 }

//                 charStack.pop();

//                 for (auto& tc : t){
//                     charStack.push(tc);
//                 }
//             }
//         }

//         t="";
//         t.resize(charStack.size());
//         int i=charStack.size() -1;

//         while (!charStack.empty()){
//             t[i] = charStack.top();
//             charStack.pop();
//             --i;
//         }

//         return t;

//     }
// };

int main(){
    Solution s;
    cout<<s.reverseParentheses("(ed(et(oc))el)");
    return 0;
}

// Input: 
// s = "(ed(et(oc))el)"
// Output: "leetcode"

// stack : 
// (ed(et(oc)
// (ed(etco)
// (edocteel)
// leetcode