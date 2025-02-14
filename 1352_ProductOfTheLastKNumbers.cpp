#include<bits/stdc++.h>
using namespace std;

class ProductOfNumbers {
    private:
    vector<int> products;

    public:
    ProductOfNumbers() {      
        products.emplace_back(1);  
    }
    
    void add(int num) {
        if (num==0){
            products = {1};
        } else {
            products.emplace_back( (*products.rbegin()) * num);
        }
    }
    
    int getProduct(int k) {
        if (k<products.size()){
            return (*products.rbegin())/(*(products.rbegin()+k)); 
        } else {
            return 0;
        }
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */