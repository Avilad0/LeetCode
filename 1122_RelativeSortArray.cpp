#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        map<int,int> freq;
        for (auto& n:arr1){
            freq[n]++;
        }

        int i=0,j;
        for (auto& n: arr2){
            for (j=0;j<freq[n];++j,++i){
                arr1[i]=n;
            }
            freq.erase(n);
        }

        for (auto& [n,f]:freq){
            for (j=0;j<f;++j,++i){
                arr1[i]=n;
            }
        }   

        return arr1;        
    }
};

int main(){
    Solution s;
    vector<int> arr1 = {2,3,1,3,2,4,6,7,9,2,19}, arr2 = {2,1,4,3,9,6};
    vector<int> ans =s.relativeSortArray(arr1,arr2);
    // Output: [2,2,2,1,4,3,3,9,6,7,19]

    for (auto& i:ans){
        cout<<i<<" ";
    }


    return 0;
}