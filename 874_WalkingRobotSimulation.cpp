#include<bits/stdc++.h>
using namespace std;

class Solution {
private:
    static const int HASH_MULTIPLIER = 60001;
    const vector<vector<int>> DIRECTIONS = {{0,1}, {1,0}, {0,-1}, {-1,0}}; //N, E, S, W

    int hash(int x, int y){
        return x + y*HASH_MULTIPLIER;
    }

public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

        unordered_set<int> hashedObstacles;
        for(auto& obs: obstacles){
            hashedObstacles.insert(hash(obs[0], obs[1]));
        }

        vector<int> currPosition = {0,0};
        int k, nextX, nextY, maxDistance=0, direction = 0; //index of DIRECTIONS
        
        for(auto& command: commands){
            if (command==-2) {
                direction = (direction+3)%4;
            } else if (command==-1) {
                direction = (direction+1)%4;
            } else {

                for(k=0;k<command;++k){
                    nextX = currPosition[0] + DIRECTIONS[direction][0];
                    nextY = currPosition[1] + DIRECTIONS[direction][1];
                    if (hashedObstacles.count(hash(nextX, nextY))!=0){
                        break;
                    }
                    currPosition[0]=nextX;
                    currPosition[1]=nextY;
                }
                maxDistance = max(maxDistance, currPosition[0]*currPosition[0] + currPosition[1]*currPosition[1]);
            }
        }

        return maxDistance;
    }
};