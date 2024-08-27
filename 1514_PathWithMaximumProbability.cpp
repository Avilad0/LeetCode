#include<bits/stdc++.h>
using namespace std;

// Beats 66.8%, Although this is slower in leetcode compared to the below method of bellman-ford, this is better according to Big-O notation.
// time: O(n + m.log(n)) , space: O(n+m)  //m=number of edges, n= number of vertex
//Dijkstra's with maxHeap
class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        vector<vector<pair<int,double>>> allEdgesWithProbability(n, vector<pair<int,double>>());
        for (int i=0;i<edges.size();++i){
            allEdgesWithProbability[edges[i][0]].emplace_back(edges[i][1], succProb[i]);
            allEdgesWithProbability[edges[i][1]].emplace_back(edges[i][0], succProb[i]);
        }


        vector<double> maxProb(n,0);
        maxProb[start_node]=1.0;
        
        priority_queue<pair<double,int>> queue;
        queue.push({1.0, start_node});

        while (!queue.empty()){

            auto [currProb, currNode] = queue.top();
            queue.pop();
            if (currNode==end_node) return currProb;

            for (auto [nextNode, nextProb]: allEdgesWithProbability[currNode]){
                if (currProb*nextProb > maxProb[nextNode]){
                    maxProb[nextNode] = currProb*nextProb;
                    queue.push({maxProb[nextNode], nextNode});
                }
            }
        }

        return 0;
    }
};

int main(){
    Solution s;
    int n=3, start_node=0, end_node=2;
    vector<vector<int>> edges = {{0,1},{1,2},{0,2}};
    vector<double> succProb = {0.5,0.5,0.2};

    cout<<s.maxProbability(n,edges, succProb, start_node, end_node);
    return 0;
}

// beats 99.8%
// Bellman-Ford, time: O(n.m) , space: O(n)  //m=number of edges, n= number of vertex
// class Solution {
// public:
//     double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
//         vector<double> maxProb(n,0);
//         maxProb[start_node]=1.0;
//         bool isChanged;

//         for(int i=0;i<n-1;++i){
//             isChanged=false;
//             for (int j=0;j<edges.size();++j){
//                 if (maxProb[edges[j][0]]*succProb[j]> maxProb[edges[j][1]]){
//                     maxProb[edges[j][1]]= maxProb[edges[j][0]]*succProb[j];
//                     isChanged=true;
//                 }

//                 if (maxProb[edges[j][1]]*succProb[j]> maxProb[edges[j][0]]){
//                     maxProb[edges[j][0]]= maxProb[edges[j][1]]*succProb[j];
//                     isChanged=true;
//                 }
//             }
//             if(!isChanged)break;
//         }

//         return maxProb[end_node];
//     }
// };



// TLE for very large cases >5000
// class Solution {
// public:
//     double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
//         allEdgesWithProbability = vector<vector<pair<int,double>>>(n, vector<pair<int,double>>());
//         for (int i=0;i<edges.size();++i){
//             allEdgesWithProbability[edges[i][0]].emplace_back(edges[i][1], succProb[i]);
//             allEdgesWithProbability[edges[i][1]].emplace_back(edges[i][0], succProb[i]);
//         }

//         visit(end_node, start_node, 1);

//         return maxProb;
//     }

// private:
//     vector<vector<pair<int,double>>> allEdgesWithProbability;
//     unordered_set<int> visited;
//     double maxProb = 0;

//     void visit(int& end_node, int currNode, double probability){

//         if (end_node==currNode){
//             maxProb = max(probability, maxProb);
//             return;
//         }

//         if (probability<=maxProb) return;

//         visited.insert(currNode);
//         for (auto& [node, nodeProb]: allEdgesWithProbability[currNode]){
//             if (visited.find(node) == visited.end()){
//                 visit(end_node, node, probability*nodeProb);
//             }
//         }
//         visited.erase(currNode);
//     }
// };