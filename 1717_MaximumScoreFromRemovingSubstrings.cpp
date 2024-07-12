#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumGain(string s, int x, int y) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        vector<pair<string,int>> searches(2);

        if (x>=y){
            searches[0] = {"ab", x};
            searches[1] = {"ba", y};

        } else{
            searches[0] = {"ba", y};
            searches[1] = {"ab", x};
        }

        int ans = 0, i, writeIndex;
        for (auto& [searchString, value] : searches){
            for (i=1, writeIndex=1; i<s.length(); ++i){
                s[writeIndex++] = s[i];
                if ( writeIndex>1 && s[writeIndex-2] == searchString[0] && s[writeIndex-1]== searchString[1]){
                    ans+=value;
                    writeIndex-=2;
                }
            }

            s.erase( s.begin() + writeIndex, s.end());
        }

        return ans;
    }
};


int main(){
    Solution s;
    // cout<<s.maximumGain("cdbcbbaaabab",4,5);
    cout<<s.maximumGain("aabbaaxybbaabb",5,4);
    return 0;
}

// Input: 
// s = "cdbcbbaaabab", x = 4, y = 5
// cdbcbbaaabab
// cdbcbaab
// cdbcab
// cdbc
// Output: 19

// cdbcbbaaabab
// cdbcabab