#include<bits/stdc++.h>
using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        vector<vector<int>> matrix(m, vector<int>(n,-1));

        int currentDir=0, i=0,j=-1, _ , currLoop;
        vector<pair<int,int>> directions = {{0,1},{1,0},{0,-1},{-1,0}};
        --m;
        while (head){
            currLoop = currentDir%2==0? n:m;
            for(_=0;head && _<currLoop; ++_){
                i+=directions[currentDir].first;
                j+=directions[currentDir].second;
                matrix[i][j]=head->val;
                head=head->next;
            }
            currentDir%2==0? --n:--m;
            currentDir = (currentDir+1)%4;
        }

        return matrix;        
    }
};