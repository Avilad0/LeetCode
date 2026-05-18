class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)

        costPrev2, costPrev1 = cost[0], cost[1]
        for i in range(2,n):
            costPrev2, costPrev1 = costPrev1 , cost[i] + min(costPrev2, costPrev1)
            # currCost = cost[i] + min(costPrev2, costPrev1)
            # costPrev2 = costPrev1
            # costPrev1 = currCost 
        
        return min(costPrev1, costPrev2)