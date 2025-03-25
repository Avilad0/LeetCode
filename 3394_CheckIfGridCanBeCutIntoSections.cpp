#include<bits/stdc++.h>
using namespace std;

// can also do in-place sorting twice for 0th and 1st place in rectangle but may not be good option in interview.

class Solution {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> minHeapX, minHeapY;
        
        for (auto& r: rectangles){
            minHeapX.emplace(r[0],r[2]);
            minHeapY.emplace(r[1],r[3]);
        } 
        int prevEndX = minHeapX.top().second;
        minHeapX.pop();
        int prevEndY = minHeapY.top().second;
        minHeapY.pop();

        int validCutsX = 0, validCutsY=0;
        while (!minHeapX.empty()){
            int startX = minHeapX.top().first, endX = minHeapX.top().second;
            minHeapX.pop();

            if (startX>=prevEndX){
                validCutsX++;
                prevEndX = endX;
            } else if( endX > prevEndX){
                prevEndX = endX;
            }

            if (validCutsX>=2)   return true;

            int startY = minHeapY.top().first, endY = minHeapY.top().second;
            minHeapY.pop();

            if (startY>=prevEndY){
                validCutsY++;
                prevEndY = endY;
            } else if( endY > prevEndY){
                prevEndY = endY;
            }

            if (validCutsY>=2)   return true;
        }

        return false;
    }
};


// class Solution {
// public:
//     bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
//         priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> minHeap;
        
//         //x-coordinates
//         for (auto& r: rectangles){
//             minHeap.emplace(r[0],r[2]);
//         } 
//         int prevEnd = minHeap.top().second;
//         minHeap.pop();

//         int validCuts = 0;
//         while (!minHeap.empty()){
//             int start = minHeap.top().first, end = minHeap.top().second;
//             minHeap.pop();
//             if (start>=prevEnd){
//                 validCuts++;
//                 prevEnd = end;
//             } else if( end > prevEnd){
//                 prevEnd = end;
//             }

//             if (validCuts>=2)   return true;
//         }

//         // y-coordinates
//         for (auto& r: rectangles){
//             minHeap.emplace(r[1],r[3]);
//         } 
//         prevEnd = minHeap.top().second;
//         minHeap.pop();

//         validCuts = 0;
//         while (!minHeap.empty()){
//             int start = minHeap.top().first, end = minHeap.top().second;
//             minHeap.pop();
//             if (start>=prevEnd){
//                 validCuts++;
//                 prevEnd = end;
//             } else if( end > prevEnd){
//                 prevEnd = end;
//             }

//             if (validCuts>=2)   return true;
//         }

//         return false;
//     }
// };


int main(){
    Solution s;
    int n = 4;
    vector<vector<int>> rectangles = {{0,2,2,4},{1,0,3,2},{2,2,3,4},{3,0,4,2},{3,2,4,4}};
    cout<<s.checkValidCuts(n, rectangles);
    
    return 0;
}