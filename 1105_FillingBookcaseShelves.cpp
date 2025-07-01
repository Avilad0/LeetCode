#include<bits/stdc++.h>
using namespace std;

class Solution {

private:
    unordered_map<string, int> memo;
     
    int dfs(const vector<vector<int>>& books, const int& shelfWidth, int index, int currShelfHeight, int remainingShelfWidth){
        if (index == books.size()){
            return currShelfHeight;
        }

        string key = to_string(index) + "," + to_string(remainingShelfWidth);
        if (memo.find(key) != memo.end()){
            return memo[key];
        }
        
        int placeOnSameShelf = INT_MAX;
        if (remainingShelfWidth >= books[index][0]) 
            placeOnSameShelf = dfs(books, shelfWidth, index+1, max(currShelfHeight,books[index][1]), remainingShelfWidth-books[index][0]); 

        int placeOnNextShelf = INT_MAX;
        if (currShelfHeight != 0)
            placeOnNextShelf = currShelfHeight + dfs(books, shelfWidth, index+1, books[index][1], shelfWidth-books[index][0]);

        return memo[key] = min(placeOnNextShelf, placeOnSameShelf);
    }

public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        return dfs(books, shelfWidth, 0, 0, shelfWidth);
    }
};