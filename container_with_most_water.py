class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        i = 0
        j = len(height)-1
        while(i<j):
            temp = 0
            if height[i] < height[j]:
                temp = height[i] * (j-i)
                i+=1
            elif height[i] > height[j]:
                temp = height[j] * (j-i)
                j-=1
            else:
                temp = height[i] * (j-i)
                i+=1
                j-=1
                print(temp)
            maxi = max(maxi,temp)
        return maxi
