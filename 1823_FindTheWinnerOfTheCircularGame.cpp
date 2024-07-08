#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTheWinner(int n, int k) {
        vector<int> game;
        int i;
        for (i=1;i<=n;++i)  game.push_back(i);

        i=0; --k;
        while (game.size()>1){
            i= (i+k) % game.size();
            game.erase(game.begin()+i);
        }

        return game[0];
    }
};