class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxList = []
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         if(prices[i]<prices[j]):
        #             maxList.append(prices[j]-prices[i])
        # if len(maxList)==0:
        #     return 0
        # return max(maxList)
        
        # update the relative minimum value as the list iterates.
        # and check if the difference is the greatest value.
        
        minValue = 99999
        maxValue = 0
        for i in range(0,len(prices)):
            if prices[i]<minValue:
                minValue = prices[i]
            elif prices[i]-minValue > maxValue:
                maxValue = prices[i]-minValue
        return maxValue
            
        
        
        
        
        
        
        
        
