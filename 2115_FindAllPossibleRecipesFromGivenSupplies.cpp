#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        unordered_set<string> suppliesSet(supplies.begin(), supplies.end());

        int n = recipes.size();

        unordered_map<string, int> recipeIndex;
        for (int i=0; i<n; ++i){
            recipeIndex[recipes[i]] = i;
        }

        vector<int> indegree(n,0);
        vector<vector<int>> dependentList(n, vector<int>());

        queue<int> queueRecipes;

        for (int i=0; i<n; ++i){
            for (auto& ingredient: ingredients[i]){
                if (suppliesSet.find(ingredient)==suppliesSet.end()){
                    if (recipeIndex.find(ingredient)!=recipeIndex.end()){
                        dependentList[recipeIndex[ingredient]].push_back(i);
                    }
                    indegree[i]++;
                }
            }
            if (indegree[i]==0){
                queueRecipes.push(i);
            }
        }

        vector<string> ans;
        while (!queueRecipes.empty()){
            int recipeIndex = queueRecipes.front();
            queueRecipes.pop();
            ans.push_back(recipes[recipeIndex]);

            for (auto& dependentRecipe: dependentList[recipeIndex]){
                --indegree[dependentRecipe];
                if (indegree[dependentRecipe]==0){
                    queueRecipes.push(dependentRecipe);
                }
            }
        }

        return ans;
    }
};