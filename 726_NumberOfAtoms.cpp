#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string countOfAtoms(string formula) {
        i=0;
        n = formula.length();
        unordered_map<string,int> freq = count(formula);
        
        map<string,int> freqSorted(freq.begin(), freq.end());

        string result = "";
        for (auto& [key, value]: freqSorted){
            result += key;
            if (value>1) result+=to_string(value);
        }

        return result;
    }

private:
    int i,n;

    unordered_map<string, int> count( string& formula){
        unordered_map<string, int> freq;
        string name;
        int multiplier;
        while ( i<n && formula[i]!=')' ){

            if (formula[i]=='('){
                ++i;
                unordered_map<string, int> subfreq = count(formula);
                ++i;

                multiplier = 0;
                while (i<n && isdigit(formula[i])){
                    multiplier= multiplier*10 + (formula[i++]-'0');
                }
                multiplier = max(multiplier, 1);
                
                for (auto& [key, value] : subfreq){
                    freq[key]+= (value* multiplier);
                }
                
            } else {
                
                name = formula[i++];
                while (i<n && islower(formula[i])){
                    name+=formula[i++];
                }

                multiplier=0;
                while (i<n && isdigit(formula[i])){
                    multiplier= multiplier*10 + (formula[i++]-'0');
                }
                freq[name]+= max(multiplier, 1);
            }
            
        }

        return freq;
    }
};

int main(){
    Solution s;
    cout<<s.countOfAtoms("H2O")<<endl;
    cout<<s.countOfAtoms("Mg(OH)2")<<endl;
    cout<<s.countOfAtoms("K4(ON(SO3)2)2")<<endl;

    return 0;
}