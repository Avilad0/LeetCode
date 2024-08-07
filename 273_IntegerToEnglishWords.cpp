#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    string numberToWords(int num) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        if (num==0) return "Zero";

        vector<string> numbers({"","One ","Two ","Three ","Four ","Five ","Six ","Seven ","Eight ","Nine ","Ten ","Eleven ","Twelve ","Thirteen ","Fourteen ","Fifteen ","Sixteen ","Seventeen ","Eighteen ","Nineteen "});
        vector<string> tensPlaces({"","Ten ","Twenty ","Thirty ","Forty ","Fifty ","Sixty ","Seventy ","Eighty ","Ninety "});

        int currDigits;
        string numberInWords ="", temp, hundred ="Hundred ";
        for (auto& suffix: {"","Thousand ","Million ","Billion "}){
            currDigits = num%1000;
            num/=1000;
            if (currDigits==0) continue;

            if (currDigits>99) temp = numbers[currDigits/100] + hundred;
            else                     temp = "";

            currDigits%=100;
            if (currDigits>19) {
                temp += tensPlaces[currDigits/10];
                if (currDigits%10 != 0) temp += numbers[currDigits%10];
            }
            else if(currDigits>0) temp+=numbers[currDigits];

            numberInWords = temp + suffix + numberInWords;

            if (num==0) break;
        }

        numberInWords.pop_back();
        return numberInWords;
    }
};