#include<bits/stdc++.h>
using namespace std;

//Floyd warshall algo [correct]
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        vector<vector<long long>> costMatrix(26, vector<long long>(26, INT_MAX));
        int i,j,k;
        
        for (i=0; i<cost.size(); ++i){
            costMatrix[original[i]-'a'][changed[i]-'a'] = min( costMatrix[original[i]-'a'][changed[i]-'a'], (long long)cost[i]);
        }

        for (k=0;k<26;++k){
            for (i=0;i<26;++i){
                for (j=0;j<26;++j){
                    costMatrix[i][j] = min(costMatrix[i][k]+ costMatrix[k][j], costMatrix[i][j]);
                }
            }
        }

        long long totalCost = 0;
        for (i=0; i<source.size(); ++i){
            if (source[i]==target[i]) continue;

            if (costMatrix[source[i]-'a'][target[i]-'a'] >= INT_MAX){
                return -1;
            }
            totalCost+=costMatrix[source[i]-'a'][target[i]-'a'];
        }

        return totalCost;
    }
};

// [wrong method]
// class Solution {
// private:
//     unordered_map<char, unordered_map<char, int>> costMap, minCostMap;
//     unordered_set<char> visited;

//     long long minPath(char source, char target){
        
//         if (source==target) 
//             return 0;
//         if (minCostMap.find(source)!=minCostMap.end() && minCostMap[source].find(target)!=minCostMap[source].end()) 
//             return minCostMap[source][target];

//         int minRunningCost = -1, t;
//         visited.insert(source);
//         for (auto& [nextChar, cost]: costMap[source]){
//             if (visited.find(nextChar) != visited.end()) continue;

//             t = minPath(nextChar, target);

//             if (t!=-1 && ( (t+cost)<minRunningCost || minRunningCost==-1)) minRunningCost = t+cost;
//         }

//         visited.erase(source);

//         return minRunningCost;
//     }

// public:
//     long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
//         long long totalCost = 0, t;        
//         int i;

//         for (i=0; i<cost.size(); ++i){
//             costMap[original[i]][changed[i]] = cost[i];
//         }

//         for (i=0; i<source.length(); ++i){
//             t = minPath(source[i], target[i]);
            
//             if (t==-1) return -1;

//             minCostMap[source[i]][target[i]] = t;
//             totalCost+=t;
//         }

//         return totalCost;
//     }
// };

int main(){
    Solution s;
    // string source = "abcd", target = "acbe";
    // vector<char> original = {'a','b','c','c','e','d'}, changed = {'b','c','b','e','b','e'};
    // vector<int> cost = {2,5,5,1,2,20};
    // output: 28

    // string source = "aaadbdcdac", target = "cdbabaddba";
    // vector<char> original = {'a','c','b','d','b','a','c'}, changed = {'c','a','d','b','c','b', 'd'};
    // vector<int> cost = {7,2,1,3,6,1,7};
    // output: 39
    // 7 + 2 + 1 + 11 + 0 + 11 + 4 + 0 + 1 + 2 = 39
    // a: [b,1], [c,7]
    // b: [c,6], [d,1]
    // c: [a,2], [d,7]
    // d: [b,3]
    // cabd,cd = 4, 7

    string source = "aabdbaabaa", target = "bdaacabcab";
    vector<char> original = {'b','d','d','a','c','c','a','d','a','b'}, changed = {'c','c','b','d','b','d','b','a','c','a'};
    vector<int> cost = {9,1,7,9,2,1,3,8,8,2};
    // output: 43
    // 3 + 9 + 2 + 5 + 9 + 0 + 3 + 9 + 0 + 3 = 43
    // a: [d,9], [b,3], [c, 8]
    // b: [c,9], [a,2]
    // c: [b,2], [d,1]
    // d: [a,8], [b,7], [c,1]
    // 
    // ab=3, ad=9, ba=2, da=5, bc=9, 
    cout<<s.minimumCost(source, target, original, changed, cost);

    return 0;
}




    // long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {

    //     long long totalCost = 0;        
    //     int i, minRunningCost;

    //     for (i=0; i<cost.size(); ++i){
    //         costMap[original[i]][changed[i]] = cost[i];
    //     }

    //     for (i=0; i<source.length(); ++i){
    //         if (source[i]==target[i]) 
    //         continue;

    //         if (minCostMap.find(source[i])!=minCostMap.end() && minCostMap[source[i]].find(target[i])!=minCostMap[source[i]].end()){
    //             totalCost+=minCostMap[source[i]][target[i]];
    //             continue;
    //         }

    //         minRunningCost = -1;
    //         queue<pair<char,int>> charQueue({{source[i],0}});
    //         unordered_set<char> visited;
    //         while (!charQueue.empty()){
                            
    //             if (charQueue.front().first == target[i] && (minRunningCost>charQueue.front().second || minRunningCost==-1)){
    //                 minRunningCost = charQueue.front().second;
    //             } else{
    //                 visited.insert(charQueue.front().first);
    //                 for (auto& [a,b]: costMap[charQueue.front().first]){
    //                     if (visited.find(a) == visited.end()){
    //                         charQueue.push({a, b+charQueue.front().second});
    //                     }
    //                 }
    //             }

    //             charQueue.pop();
    //         }

    //         if (minRunningCost == -1) return -1;

    //         totalCost+=minRunningCost;
    //         minCostMap[source[i]][target[i]]= minRunningCost;
    //     }

    //     return totalCost;
    // }