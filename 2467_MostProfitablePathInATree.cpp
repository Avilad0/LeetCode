#include<bits/stdc++.h>
using namespace std;

/*
additionally we can also use hashmap to store bobpath with time as {bobNode:time}
we can add it in alice if bobPath[bobNode] > aliceTime
or half of amount if equal
or 0
This will prevent manupulation of amount vector.
*/

class Solution {
public:
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        n = amount.size();
        vector<vector<int>> adjList(n);
        for (vector<int>& e: edges){
            adjList[e[0]].emplace_back(e[1]);
            adjList[e[1]].emplace_back(e[0]);
        }

        bobPath.emplace_back(bob);
        findBobPath(adjList, bob, -1);

        findAliceMaxSum(adjList, amount, 0, -1, 0, 0);
        return aliceMaxSum;
    }

private:
    int n;
    int aliceMaxSum =INT_MIN;
    void findAliceMaxSum(vector<vector<int>>& adjList, vector<int>& amount, int node, int parent, int sum, int time){

        int t, bobNode;
        if (bobPath.size()>time){
            bobNode = *(bobPath.begin() + time);
            t=amount[bobNode];
            if (node == bobNode){
                amount[bobNode]/=2;
            } else {
                amount[bobNode]=0;
            }
        } 

        sum+=amount[node];
        
        if (adjList[node].size()==1 && node!=0){
            aliceMaxSum = max(aliceMaxSum, sum);
        } else {
            for (int& neighbor: adjList[node]){
                if (neighbor != parent){
                    findAliceMaxSum(adjList, amount, neighbor, node, sum, time+1);
                }
            }
        }

        if (bobPath.size()>time){
            amount[bobNode]=t;
        }
    }

    vector<int> bobPath;
    bool findBobPath(vector<vector<int>>& adjList, int node, int parent){
        if (node==0) return true;

        for (int& neighbor: adjList[node]){
            if (neighbor != parent){
                bobPath.emplace_back(neighbor);
                if (findBobPath(adjList, neighbor, node)){
                    return true;
                }
                bobPath.pop_back();
            }
        }
        return false;
    }
};

int main(){
    Solution s;
    vector<vector<int>> edges = {{0,1},{1,2},{1,3},{3,4}};
    int bob = 3;
    vector<int> amount = {-2,4,2,-4,6};
    cout<<s.mostProfitablePath(edges, bob, amount);
    return 0;
}