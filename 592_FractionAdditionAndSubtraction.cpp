#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string fractionAddition(string expression) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        int i, j=0, n = expression.size(), denominatorsMultiplied=1, numeratorsAdded=0;
        vector<int> numerators, denominators;
        string negativePrefix = "";

        while (j<n){

            i=j;
            while(j<n && expression[j]!='/') ++j;
            numerators.push_back(stoi(expression.substr(i, j-i)));

            i= ++j;
            while(j<n && expression[j]!='+' && expression[j]!='-') ++j;
            denominators.push_back(stoi(expression.substr(i, j-i)));
            denominatorsMultiplied*= *denominators.rbegin();
        }
        
        for (i=0;i<numerators.size();++i){
            numeratorsAdded+= numerators[i]*denominatorsMultiplied/denominators[i];
        }

        if (numeratorsAdded==0) return "0/1";
        
        if (numeratorsAdded<0){
            negativePrefix = "-";
            numeratorsAdded*= -1;
        }

        //alternately can use euclids algorithm below
        i=2;
        while ( (i*i)<=numeratorsAdded && (i*i)<=denominatorsMultiplied){
            while ((denominatorsMultiplied%i == 0) && (numeratorsAdded%i == 0)) {
                denominatorsMultiplied/=i;
                numeratorsAdded/=i;
            }
            ++i;
        }

        return negativePrefix + to_string(numeratorsAdded) + "/" + to_string(denominatorsMultiplied);
    }
};


int main(){
    Solution s;
    // string ex = "-1/2+1/2";
    // string ex = "-1/2+1/2+1/3";
    // string ex = "1/3-1/2";
    string ex = "-1/4-4/5-1/4";

    cout<<s.fractionAddition(ex);
    return 0;
}