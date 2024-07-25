#include<bits/stdc++.h>
using namespace std;

//heap sort
class Solution {

private:
    void heapify(vector<int>& nums, int size, int i){
       
        int largest = i;


        int l = 2 * i + 1, r = 2 * i + 2;

        if (l < size && nums[l] > nums[largest]) largest = l;
        if (r < size && nums[r] > nums[largest]) largest = r;

        if (largest != i) {
            swap(nums[i], nums[largest]);
            heapify(nums, size, largest);
        }
    }

public:
    vector<int> sortArray(vector<int>& nums) {
        ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
        
        int size = nums.size();
        for (int i = size/2 -1; i>=0; --i) heapify(nums, size, i);
        
        for (int i = size - 1; i > 0; i--) {
            swap(nums[0], nums[i]);
            heapify(nums, i, 0);
        }
        return nums;
    }
};







//quick sort - TLE
// class Solution {
// private:

// int partition(vector<int>& nums, int low, int high){
//     int pivot = nums[high];

//     int left=low-1;

//     for (int right=low; right<high; ++right){
//         if (nums[right]<pivot){
//             ++left;
//             swap(nums[left], nums[right]);
//         }
//     }
    
//     ++left;
//     swap(nums[left], nums[high]);

//     return left;
// }

// void quicksort(vector<int>& nums, int low, int high){
//     if (low<high){

//         int partitionIndex = partition(nums, low, high);

//         quicksort(nums, low, partitionIndex-1);
//         quicksort(nums, partitionIndex+1, high);
//     }

// }

// public:
//     vector<int> sortArray(vector<int>& nums) {
//         ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
//         quicksort(nums, 0, nums.size()-1);
//         return nums;
//     }
// };