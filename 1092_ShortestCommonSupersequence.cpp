#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string shortestCommonSupersequence(string str1, string str2) {
        int n1 = str1.size(), n2 = str2.size(), i ,j;

        vector<vector<int>> dp(n1+1, vector<int>(n2+1,0));
        for (i=1; i<=n1; ++i)   dp[i][0]=i;
        for (j=1; j<=n2; ++j)   dp[0][j]=j;

        for (i=1; i<=n1; ++i){
            for (j=1; j<=n2; ++j){
                if (str1[i-1]==str2[j-1]){
                    dp[i][j] = dp[i-1][j-1]+1;
                } else {
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1;
                }
            }
        }

        string supersequence = "";
        i=n1;
        j=n2;
        while (i>0 && j>0){
            if (str1[i-1]==str2[j-1]) {
                supersequence += str1[i-1];
                i--;
                j--;
            } else if (dp[i-1][j] < dp[i][j-1]) {
                supersequence += str1[i-1];
                i--;
            } else {
                supersequence += str2[j-1];
                j--;
            }
        }

        while (i>0){
            supersequence+=str1[(i--)-1];
        }
        while (j>0){
            supersequence+=str2[(j--)-1];
        }

        reverse(supersequence.begin(), supersequence.end());
        return supersequence;
    }
};